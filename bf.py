# BF Manager - Blox Fruits multi-account launcher + auto-rejoin (Termux / Android)
#
# Based on the AJ V2 manager (github.com/aaalmaz0/mm2 nub.py), retargeted from
# MM2 to Blox Fruits. Strips the Discord bot, Delta key system, WebSocket relay
# and in-game executor logic - this is just a launcher/babysitter:
#
#   * launches every Roblox clone into its assigned sea
#   * watches all of them and reopens any that crash
#   * rejoins any that get bounced to the website or drop out of the game
#
# Run it with:  python bf.py

import os
import sys
import json
import time
import builtins
import threading
import subprocess

import requests
from colorama import init, Fore, Style

try:
    import pyfiglet
except ImportError:
    pyfiglet = None
try:
    from prettytable import PrettyTable
except ImportError:
    PrettyTable = None

init(autoreset=True)

# ---------------------------------------------------------------- config

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SETTINGS_FILE = os.path.join(SCRIPT_DIR, 'bf.txt')
ACCOUNTS_FILE = os.path.join(SCRIPT_DIR, 'bf_accounts.txt')
CACHE_FILE = os.path.join(SCRIPT_DIR, 'bf_usernames.json')

# Blox Fruits is one universe with a separate place per sea. Joining a 2nd/3rd
# sea place only sticks if the account has actually unlocked that sea in-game -
# otherwise Roblox drops it back to the First Sea. The manager can only aim at
# the place; account progression decides whether it holds.
BLOX_FRUITS_UNIVERSE = 994732206
SEAS = {
    1: 2753915549,   # First Sea  (main Blox Fruits place)
    2: 4442272183,   # Second Sea
    3: 7449423635,   # Third Sea
}
SEA_NAMES = {1: 'First Sea', 2: 'Second Sea', 3: 'Third Sea'}

SWEEP_DELAY = 90          # seconds between full presence+process sweeps
PER_PACKAGE_DELAY = 20    # pause between accounts in a sweep (keeps under the presence API rate limit)
WATCHDOG_INTERVAL = 5     # fast process-liveness check
LAUNCH_GRACE = 75         # don't judge a clone as crashed for this long after launching it
REOPEN_COOLDOWN = 60      # min gap between reopen attempts for the same clone
NOT_IN_GAME_LIMIT = 180   # app alive but not in Blox Fruits for this long -> force a rejoin

CONFIG = {'default_sea': 1, 'accounts': {}}
username_cache = {}

_launch_locks = {}
_launch_guard = threading.Lock()
_launched_at = {}
_reopened_at = {}
_last_in_game_at = {}   # last time the presence sweep confirmed this clone in Blox Fruits
_state_lock = threading.Lock()

IN_GAME_TRUST = 150   # skip a process-based reopen if presence saw it in-game this recently


def _launch_gap(num_packages):
    """More clones = slower device = give each one longer to come up."""
    return 16 if num_packages >= 6 else 9


# ---------------------------------------------------------------- console (pinned status table)

_bottom_table = None
_bottom_lines = 0


def _erase_bottom():
    global _bottom_lines
    if _bottom_lines:
        sys.stdout.write('\033[{}A\033[0J'.format(_bottom_lines))
        _bottom_lines = 0


def _draw_bottom():
    global _bottom_lines
    if _bottom_table is not None:
        builtins.print(_bottom_table)
        _bottom_lines = _bottom_table.count('\n') + 1


def _log_print(*args, **kwargs):
    """Print a log line ABOVE the pinned status table so logs scroll while the
    table stays put at the bottom and updates in place."""
    if not sys.stdout.isatty():
        builtins.print(*args, **kwargs)
        return
    _erase_bottom()
    builtins.print(*args, **kwargs)
    _draw_bottom()


print = _log_print


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header():
    if pyfiglet:
        print(Fore.LIGHTYELLOW_EX + pyfiglet.figlet_format('BF Mgr', font='standard') + Style.RESET_ALL)
    else:
        print(Fore.LIGHTYELLOW_EX + '=== BF Manager ===' + Style.RESET_ALL)


def update_status_table(statuses):
    global _bottom_table
    if PrettyTable is None:
        return
    table = PrettyTable()
    table.field_names = ['Package', 'Username', 'Sea', 'Status']
    table.align = 'l'
    for package, info in statuses.items():
        table.add_row([package, info.get('Username', '?'), info.get('Sea', '?'), info.get('Status', '')])
    rendered = str(table)
    if rendered == _bottom_table:
        return
    if not sys.stdout.isatty():
        _bottom_table = rendered
        builtins.print(rendered)
        return
    _erase_bottom()
    _bottom_table = rendered
    _draw_bottom()


def set_status(statuses, package_name, colour, text):
    if package_name in statuses:
        statuses[package_name]['Status'] = colour + text + Style.RESET_ALL
        update_status_table(statuses)


# ---------------------------------------------------------------- settings (bf.txt)

def load_settings():
    global CONFIG
    if os.path.exists(SETTINGS_FILE):
        try:
            with open(SETTINGS_FILE, 'r') as f:
                data = json.load(f)
            if isinstance(data, dict):
                CONFIG = data
        except (IOError, ValueError):
            pass
    CONFIG.setdefault('default_sea', 1)
    CONFIG.setdefault('accounts', {})


def save_settings():
    try:
        with open(SETTINGS_FILE, 'w') as f:
            json.dump(CONFIG, f, indent=2)
    except IOError as e:
        print(Fore.RED + 'Could not save bf.txt: {}'.format(e) + Style.RESET_ALL)


def ensure_settings(packages):
    """Load bf.txt, or run a short first-time setup: one default sea for
    everyone, plus optional per-account overrides."""
    load_settings()
    if os.path.exists(SETTINGS_FILE):
        return

    print(Fore.YELLOW + 'First-time setup.' + Style.RESET_ALL)
    raw = input('Default sea for all accounts  1=First  2=Second  3=Third  [1]: ').strip()
    CONFIG['default_sea'] = int(raw) if raw in ('1', '2', '3') else 1
    CONFIG['accounts'] = {}

    print('Detected packages:')
    for p in packages:
        print('  ' + p)
    over = input(
        "Per-account sea overrides? e.g.  com.roblox.clientalpha=2, com.roblox.clientbeta=3\n"
        "(Enter to put every account on sea {}): ".format(CONFIG['default_sea'])).strip()
    if over:
        for part in over.split(','):
            if '=' in part:
                k, v = part.split('=', 1)
                k, v = k.strip(), v.strip()
                if v in ('1', '2', '3'):
                    CONFIG['accounts'][k] = int(v)
    save_settings()
    print(Fore.GREEN + 'Saved to bf.txt' + Style.RESET_ALL)


def sea_for(package_name):
    return CONFIG['accounts'].get(package_name, CONFIG.get('default_sea', 1))


# ---------------------------------------------------------------- packages

def get_roblox_packages():
    packages = []
    try:
        output = subprocess.check_output('pm list packages', shell=True, text=True)
    except subprocess.CalledProcessError:
        print(Fore.RED + 'Could not list packages (is this Termux on Android?).' + Style.RESET_ALL)
        return packages
    print(Fore.YELLOW + 'Scanning for Roblox packages...' + Style.RESET_ALL)
    for line in output.splitlines():
        if 'com.roblox.' in line:
            package_name = line.split(':')[1].strip()
            print(Fore.GREEN + 'Found: ' + package_name + Style.RESET_ALL)
            packages.append(package_name)
    if not packages:
        print(Fore.RED + 'No Roblox packages found.' + Style.RESET_ALL)
    return packages


def proc_cmdlines():
    """One blob of every process's full cmdline, from /proc/<pid>/cmdline.
    Uses the real launch string, not `ps`/comm which Android truncates to 15
    chars - that truncation is why a plain `com.roblox.clientalpha` match fails.
    Needs root (which the run command uses); returns '' if /proc is locked down."""
    parts = []
    try:
        pids = [p for p in os.listdir('/proc') if p.isdigit()]
    except OSError:
        return ''
    for pid in pids:
        try:
            with open('/proc/{}/cmdline'.format(pid), 'rb') as f:
                parts.append(f.read().replace(b'\x00', b' ').decode('utf-8', 'ignore'))
        except (IOError, OSError):
            continue
    return '\n'.join(parts)


def is_roblox_running(package_name, proc_blob=None):
    """True if a process for this package is alive. Prefers /proc scanning;
    only shells out to pgrep/pidof when /proc is unreadable (no root)."""
    blob = proc_blob if proc_blob is not None else proc_cmdlines()
    if blob:
        return package_name in blob
    for cmd in (['pgrep', '-f', package_name], ['pidof', package_name]):
        try:
            r = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
            if r.stdout.strip():
                return True
        except (OSError, subprocess.SubprocessError):
            pass
    return False


def kill_roblox_process(package_name):
    print('Killing {}...'.format(package_name))
    os.system('pkill -f ' + package_name)
    time.sleep(2)


def kill_all(accounts):
    print('Killing all Roblox clones...')
    for package_name, _ in accounts:
        os.system('pkill -f ' + package_name)
    time.sleep(2)


# ---------------------------------------------------------------- launch

def launch_roblox(package_name, sea, num_packages, statuses):
    place_id = SEAS.get(sea, SEAS[1])
    uri = 'roblox://placeID={}'.format(place_id)
    name = SEA_NAMES.get(sea, 'First Sea')
    try:
        set_status(statuses, package_name, Fore.LIGHTCYAN_EX, 'Opening app...')
        subprocess.run(
            ['am', 'start', '-n', package_name + '/com.roblox.client.startup.ActivitySplash', '-d', uri],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(_launch_gap(num_packages))

        set_status(statuses, package_name, Fore.LIGHTCYAN_EX, 'Joining {}...'.format(name))
        subprocess.run(
            ['am', 'start', '-n', package_name + '/com.roblox.client.ActivityProtocolLaunch', '-d', uri],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(4)

        with _state_lock:
            _launched_at[package_name] = time.time()
        set_status(statuses, package_name, Fore.GREEN, 'Launched -> {}'.format(name))
    except Exception as e:
        set_status(statuses, package_name, Fore.RED, 'Launch error: {}'.format(e))
        print(Fore.RED + 'Launch error for {}: {}'.format(package_name, e) + Style.RESET_ALL)


def _package_lock(package_name):
    with _launch_guard:
        return _launch_locks.setdefault(package_name, threading.Lock())


def safe_launch(package_name, num_packages, statuses, kill_first=False):
    """Launch in a background thread, lock-guarded so the monitor and the
    watchdog can never relaunch the same clone at the same time."""
    lock = _package_lock(package_name)
    if not lock.acquire(blocking=False):
        return False

    def _run():
        try:
            if kill_first:
                kill_roblox_process(package_name)
            launch_roblox(package_name, sea_for(package_name), num_packages, statuses)
        finally:
            lock.release()

    threading.Thread(target=_run, daemon=True).start()
    return True


# ---------------------------------------------------------------- accounts / usernames

def _find_userid_from_file(path):
    try:
        with open(path, 'r') as f:
            content = f.read()
        marker = '"UserId":"'
        start = content.find(marker)
        if start == -1:
            return None
        start += len(marker)
        end = content.find('"', start)
        return content[start:end] if end != -1 else None
    except IOError:
        return None


def load_accounts():
    accounts = {}
    if os.path.exists(ACCOUNTS_FILE):
        with open(ACCOUNTS_FILE, 'r') as f:
            for line in f:
                line = line.strip()
                if not line or ',' not in line:
                    continue
                pkg, uid = line.split(',', 1)
                accounts[pkg] = uid.strip()
    return accounts


def save_accounts(accounts):
    try:
        with open(ACCOUNTS_FILE, 'w') as f:
            for pkg, uid in accounts:
                if uid:
                    f.write('{},{}\n'.format(pkg, uid))
    except IOError:
        pass


def resolve_userid_from_username(username):
    for base in ('https://users.roblox.com/v1/usernames/users',
                 'https://users.roproxy.com/v1/usernames/users'):
        for _ in range(2):
            try:
                resp = requests.post(base, json={'usernames': [username], 'excludeBannedUsers': False},
                                     timeout=15)
                resp.raise_for_status()
                data = resp.json().get('data') or []
                if data:
                    return str(data[0]['id'])
                break
            except (requests.RequestException, ValueError, KeyError, IndexError):
                time.sleep(1)
    return None


def setup_accounts(packages):
    """Best-effort UserId per package: appStorage.json (root only) -> saved
    bf_accounts.txt -> prompt for the Roblox username. A package with no UserId
    still runs, just process-only (no presence checks for it)."""
    saved = load_accounts()
    accounts = []
    for package_name in packages:
        path = '/data/data/{}/files/appData/LocalStorage/appStorage.json'.format(package_name)
        user_id = _find_userid_from_file(path) or saved.get(package_name)
        if not user_id:
            entered = input('Roblox username for {} (Enter to skip presence checks): '.format(
                package_name)).strip()
            if entered:
                user_id = resolve_userid_from_username(entered)
                if not user_id:
                    print(Fore.RED + 'Could not resolve "{}".'.format(entered) + Style.RESET_ALL)
        accounts.append((package_name, user_id))
        if user_id:
            print(Fore.GREEN + '{} -> UserId {}'.format(package_name, user_id) + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + '{} -> no UserId (process-only)'.format(package_name) + Style.RESET_ALL)
    save_accounts(accounts)
    return accounts


def load_cache():
    global username_cache
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, 'r') as f:
                username_cache = json.load(f)
        except (IOError, ValueError):
            username_cache = {}


def save_cache():
    try:
        tmp = CACHE_FILE + '.tmp'
        with open(tmp, 'w') as f:
            json.dump(username_cache, f)
        os.replace(tmp, CACHE_FILE)
    except IOError:
        pass


def get_username(user_id):
    if not user_id:
        return '(process-only)'
    if user_id in username_cache:
        return username_cache[user_id]
    for base in ('https://users.roblox.com/v1/users/', 'https://users.roproxy.com/v1/users/'):
        for attempt in range(2):
            try:
                r = requests.get(base + str(user_id), timeout=10)
                r.raise_for_status()
                name = r.json().get('name', 'Unknown')
                if name != 'Unknown':
                    username_cache[user_id] = name
                    return name
            except requests.RequestException:
                time.sleep(2 ** attempt)
    return 'Unknown'


def check_presence(user_id):
    """(type, location, placeId, universeId) for a user, or None if the API
    would not answer. type: 0 offline, 1 online (app, no game), 2 in-game."""
    if not user_id:
        return None
    delay = 2
    for attempt in range(3):
        try:
            r = requests.post('https://presence.roblox.com/v1/presence/users',
                              headers={'Content-Type': 'application/json'},
                              data=json.dumps({'userIds': [int(user_id)]}), timeout=8)
            r.raise_for_status()
            p = r.json()['userPresences'][0]
            return (p.get('userPresenceType', 0), p.get('lastLocation'),
                    p.get('placeId'), p.get('universeId'))
        except (requests.RequestException, ValueError, KeyError, IndexError):
            if attempt < 2:
                time.sleep(delay)
                delay *= 2
    return None


def _sea_from_place(place_id):
    for sea, pid in SEAS.items():
        if place_id == pid:
            return sea
    return None


# ---------------------------------------------------------------- watchdog / monitor

def process_watchdog(accounts, statuses):
    """Fast loop: any clone whose process has died (and is past its launch
    grace period) gets reopened straight away, without waiting for the slow
    presence sweep."""
    num_packages = len(accounts)
    while True:
        time.sleep(WATCHDOG_INTERVAL)
        now = time.time()
        blob = proc_cmdlines()
        for package_name, _ in accounts:
            with _state_lock:
                launched = _launched_at.get(package_name, 0)
                reopened = _reopened_at.get(package_name, 0)
                in_game = _last_in_game_at.get(package_name, 0)
            if launched == 0 or now - launched < LAUNCH_GRACE:
                continue
            if now - reopened < REOPEN_COOLDOWN:
                continue
            if now - in_game < IN_GAME_TRUST:
                continue   # presence just confirmed it in-game - don't fight a flaky proc check
            if not is_roblox_running(package_name, blob):
                with _state_lock:
                    _reopened_at[package_name] = now
                set_status(statuses, package_name, Fore.RED, 'Process gone - reopening')
                safe_launch(package_name, num_packages, statuses)


def monitor(accounts, statuses):
    """Slow full sweep: for each account confirm it is actually in Blox Fruits;
    rejoin it if it is on the website, in a different game, or dropped out."""
    num_packages = len(accounts)
    not_in_game_since = {}
    while True:
        try:
            for package_name, user_id in accounts:
                try:
                    assigned = sea_for(package_name)
                    statuses[package_name]['Sea'] = SEA_NAMES.get(assigned, '?')
                    if user_id:
                        statuses[package_name]['Username'] = get_username(user_id)

                    pres = check_presence(user_id)
                    running = is_roblox_running(package_name)
                    now = time.time()
                    print('  {}: presence={} running={}'.format(
                        package_name, pres if pres else 'none', running))

                    with _state_lock:
                        fresh = now - _launched_at.get(package_name, 0) < LAUNCH_GRACE
                        cooling = now - _reopened_at.get(package_name, 0) < REOPEN_COOLDOWN

                    if pres is None:
                        # no presence data - fall back to "is the app alive"
                        if not running and not fresh and not cooling:
                            set_status(statuses, package_name, Fore.RED, 'Crashed - reopening')
                            with _state_lock:
                                _reopened_at[package_name] = now
                            safe_launch(package_name, num_packages, statuses)
                        else:
                            set_status(statuses, package_name, Fore.YELLOW, 'App up, presence unknown')
                        time.sleep(PER_PACKAGE_DELAY)
                        continue

                    ptype, location, place_id, universe_id = pres

                    if ptype == 2 and universe_id == BLOX_FRUITS_UNIVERSE:
                        not_in_game_since.pop(package_name, None)
                        with _state_lock:
                            _last_in_game_at[package_name] = now
                        sea = _sea_from_place(place_id)
                        if sea and sea != assigned:
                            set_status(statuses, package_name, Fore.GREEN,
                                       'In {} (assigned {})'.format(SEA_NAMES[sea], SEA_NAMES[assigned]))
                        else:
                            set_status(statuses, package_name, Fore.GREEN,
                                       'In {}'.format(SEA_NAMES.get(sea, 'Blox Fruits')))

                    elif location == 'Website':
                        set_status(statuses, package_name, Fore.RED, 'On website - rejoining')
                        with _state_lock:
                            _reopened_at[package_name] = now
                        safe_launch(package_name, num_packages, statuses, kill_first=True)

                    elif not running and not fresh and not cooling:
                        set_status(statuses, package_name, Fore.RED, 'Crashed - reopening')
                        with _state_lock:
                            _reopened_at[package_name] = now
                        safe_launch(package_name, num_packages, statuses)

                    else:
                        # app alive but not in Blox Fruits (menu, loading, other game)
                        since = not_in_game_since.setdefault(package_name, now)
                        stuck_for = int(now - since)
                        if stuck_for > NOT_IN_GAME_LIMIT and not fresh and not cooling:
                            set_status(statuses, package_name, Fore.RED,
                                       'Not in game {}s - rejoining'.format(stuck_for))
                            not_in_game_since.pop(package_name, None)
                            with _state_lock:
                                _reopened_at[package_name] = now
                            safe_launch(package_name, num_packages, statuses, kill_first=True)
                        else:
                            set_status(statuses, package_name, Fore.YELLOW,
                                       'Not in Blox Fruits ({}s)'.format(stuck_for))

                    time.sleep(PER_PACKAGE_DELAY)
                except Exception as e:
                    print(Fore.RED + 'Sweep error for {}: {}'.format(package_name, e) + Style.RESET_ALL)
                    set_status(statuses, package_name, Fore.RED, 'Sweep error')

            save_cache()
            time.sleep(SWEEP_DELAY)
        except Exception as e:
            print(Fore.RED + 'Monitor loop error: {}'.format(e) + Style.RESET_ALL)
            time.sleep(15)


# ---------------------------------------------------------------- main

def initial_launch(accounts, statuses):
    num_packages = len(accounts)
    kill_all(accounts)
    time.sleep(2)
    for package_name, user_id in accounts:
        try:
            set_status(statuses, package_name, Fore.LIGHTCYAN_EX, 'Launching')
            launch_roblox(package_name, sea_for(package_name), num_packages, statuses)
        except Exception as e:
            print(Fore.RED + 'Error launching {}: {}'.format(package_name, e) + Style.RESET_ALL)
            set_status(statuses, package_name, Fore.RED, 'Launch failed')


def main():
    clear_console()
    print_header()
    load_cache()

    packages = get_roblox_packages()
    if not packages:
        return

    ensure_settings(packages)
    accounts = setup_accounts(packages)
    if not accounts:
        print(Fore.RED + 'No accounts to manage.' + Style.RESET_ALL)
        return

    print(Fore.LIGHTCYAN_EX + '\nSea assignments:' + Style.RESET_ALL)
    for package_name, _ in accounts:
        print('  {} -> {}'.format(package_name, SEA_NAMES.get(sea_for(package_name), '?')))
    print()

    statuses = {
        package_name: {
            'Username': get_username(user_id),
            'Sea': SEA_NAMES.get(sea_for(package_name), '?'),
            'Status': Fore.LIGHTCYAN_EX + 'Starting' + Style.RESET_ALL,
        }
        for package_name, user_id in accounts
    }
    update_status_table(statuses)

    initial_launch(accounts, statuses)
    threading.Thread(target=process_watchdog, args=(accounts, statuses), daemon=True).start()
    monitor(accounts, statuses)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nStopped.')
