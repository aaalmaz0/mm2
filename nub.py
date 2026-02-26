import sys as _sys, os as _os
try:
    if not _sys.stdin.isatty():
        _sys.stdin = open('/dev/tty', 'r')
except Exception:
    pass

def h2o(july, *k):
    return ''.join(str(c) for c in july)

def H2SbF7(x):
    return int(x - 30583)

def c2h6(e):
    br = bytearray(e[len(b'Dreamon/'):])
    r = 0
    for b in br:
        r = r * 256 + b
    return r

def longlongint(x):
    ar = []
    for i in x:
        ar.append(eval(i))
    return ar

def o2(h2so3):
    # After deobfuscation, characters are already plain strings — pass them through.
    # If called with an obfuscated int codepoint, decode it.
    if isinstance(h2so3, str):
        return h2so3
    h2so3 = h2so3 - 16742655
    if h2so3 <= 127:
        return str(bytes([h2so3]), 'utf8')
    elif h2so3 <= 2047:
        b1 = 192 | h2so3 >> 6
        b2 = 128 | h2so3 & 63
        return str(bytes([b1, b2]), 'utf8')
    elif h2so3 <= 65535:
        b1 = 224 | h2so3 >> 12
        b2 = 128 | h2so3 >> 6 & 63
        b3 = 128 | h2so3 & 63
        return str(bytes([b1, b2, b3]), 'utf8')
    else:
        b1 = 240 | h2so3 >> 18
        b2 = 128 | h2so3 >> 12 & 63
        b3 = 128 | h2so3 >> 6 & 63
        b4 = 128 | h2so3 & 63
        return str(bytes([b1, b2, b3, b4]), 'utf8')

def _hex(j):
    h2so3 = ''
    for _hex in j:
        h2so3 += o2(_hex)
    return h2so3
import traceback, marshal
ch = set()
am = {'builtins', '__main__'}

def vv():
    raise MemoryError('>> GOOD LUCK!! CONMEMAY') from None

def cb(fn):
    if callable(fn) and fn.__module__ not in am:
        ch.add(fn.__module__)
        vv()

def ba(fn):

    def hi(*args, **kwargs):
        if args and args[0] in ch:
            vv()
        return fn(*args, **kwargs)
    return hi

def bh():
    stack = traceback.extract_stack()
    for frame in stack[:-2]:
        if frame.filename != __file__:
            vv()

def ck(fn, md):
    if callable(fn) and fn.__module__ != md:
        ch.add(md)
        raise ImportError('{}{}{}{}{}'.format('>> Detect [', fn.__name__, '] call [', md, '] ! <<')) from None

def ic(md, nf):
    module = __import__(md)
    funcs = nf if isinstance(nf, list) else [nf]
    [ck(getattr(module, func, None), md) for func in funcs]

def lf(val, xy):
    return callable(val) and xy and (val.__module__ != xy.__name__)

def kt(lo):
    if any((lf(val, xy) for val, xy in lo)):
        vv()

def ct(md, nf):
    module = __import__(md)
    func = getattr(module, nf, None)
    if func is None:
        vv()
    tg = type(func)

    def cf(func):
        if type(func) != tg:
            vv()
    cf(func)
    return func

def ic_type(md, nf):
    func = ct(md, nf)
    ck(func, md)

def nc():
    __import__('sys').settrace(lambda *args, **keys: None)
    __import__('sys').modules['marshal'] = None
    __import__('sys').modules['marshal'] = type(__import__('sys'))('marshal')
    __import__('sys').modules['marshal'].loads = marshal.loads

def sc():
    nk = {'marshal': 'loads'}
    [ic_type(md, nf) for md, nf in nk.items()]
    lo = [(__import__('marshal').loads, marshal)]
    kt(lo)
    nc()
sc()
bh()

def safe_input(prompt=''):
    while True:
        try:
            val = input(prompt)
            return val
        except KeyboardInterrupt:
            raise
        except EOFError:
            # stdin not ready yet, open /dev/tty directly
            try:
                import sys
                sys.stdin = open('/dev/tty', 'r')
            except Exception:
                pass
            continue
        except Exception:
            return ''

import os
import uuid
import requests
import json
import time
import subprocess
import asyncio
import aiohttp
import threading
import psutil
import sqlite3
import shutil
import sys
import random
import string
import re
from datetime import datetime
from colorama import init, Fore, Style
from threading import Lock
import base64
from urllib.parse import urlparse, parse_qs
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from concurrent.futures import ThreadPoolExecutor
from loguru import logger
from prettytable import PrettyTable
from colorama import Fore, Style, init
init(autoreset=True)

def set_console_title(title):
    if os.name == 'nt':
        os.system('{}{}'.format('title ', title))
set_console_title('Rokid Manager - UGPhone Rejoin')

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_authencation():
    github_raw_link = 'https://raw.githubusercontent.com/thieusitinks/Rokid-Manager/refs/heads/main/Authencator'
    try:
        response = requests.get(github_raw_link)
        response.raise_for_status()
        content = response.text.strip().lower()
        if content == 'true':
            print(Fore.GREEN + (lambda: (lambda: (lambda: h2o(list(map(o2, ['[', ' ', 'R', 'o', 'k', 'i', 'd', ' ', 'M', 'a', 'n', 'a', 'g', 'e', 'r', ' ', ']', ' ', '-', '>', ' ', 'A', 'u', 't', 'h', 'o', 'r', 'i', 'z', 'e', 'd']))))())())() + Style.RESET_ALL)
            return True
        else:
            print(Fore.RED + (lambda: (lambda: (lambda: h2o(list(map(o2, ['[', ' ', 'R', 'o', 'k', 'i', 'd', ' ', 'M', 'a', 'n', 'a', 'g', 'e', 'r', ' ', ']', ' ', '-', '>', ' ', 'N', 'o', 't', ' ', 'A', 'u', 't', 'h', 'o', 'r', 'i', 'z', 'e', 'd']))))())())() + Style.RESET_ALL)
            sys.exit(0)
    except requests.RequestException as e:
        print('{}{}'.format('An error occurred: ', e))
        sys.exit(1)
check_authencation()
SERVER_LINKS_FILE = os.path.join(os.path.expanduser('~'), 'server-link.txt')
ACCOUNTS_FILE = os.path.join(os.path.expanduser('~'), 'account.txt')
interval = None
stop_webhook_thread = False
webhook_thread = None
status_lock = Lock()
rejoin_lock = Lock()
package_statuses = {}
username_cache = {}
CACHE_FILE = os.path.join(os.path.expanduser('~'), 'username_cache.json')
cache_save_interval = 600
stop_event = threading.Event()
CONFIG_FILE = os.path.join(os.path.expanduser('~'), 'config-wh.json')
webhook_url = None
device_name = None
interval = None
stop_webhook_thread = False
webhook_thread = None
executors = {'Fluxus': '/storage/emulated/0/Fluxus/', 'Codex': '/storage/emulated/0/Codex/', 'Arceus X': '/storage/emulated/0/Arceus X/', 'Delta': '/storage/emulated/0/Delta/', 'Cryptic': '/storage/emulated/0/Cryptic/', 'VegaX': '/storage/emulated/0/VegaX/', 'Trigon': '/storage/emulated/0/Trigon/'}
workspace_paths = []
for executor, base_path in executors.items():
    workspace_paths.append('{}{}'.format(base_path, 'Workspace'))
    workspace_paths.append('{}{}'.format(base_path, 'workspace'))
lua_script_template = 'loadstring(game:HttpGet("https://raw.githubusercontent.com/thieusitinks/Rokid-Manager/refs/heads/main/Rokid-Script"))()'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    header = '  _____       _    _     _   __  __                                    |  __      | |  _)   | | |  /  |                                   | |__) |___ | | ___  __| | |   / | __ _ _ __   __ _  __ _  ___ _ __  |  _  // _ | |/ / |/ _` | | |/| |/ _` | _  / _` |/ _` |/ _  __| | |   _) |   <| | _| | | |  | | _| | | | | _| | _| |  __/ |    |_|  ____/|_|__|__,_| |_|  |_|__,_|_| |_|__,_|__, |___|_|                                                          __/ |                                                                |___/                     '
    print(Fore.LIGHTYELLOW_EX + header + Style.RESET_ALL)
    print(Fore.LIGHTYELLOW_EX + 'Developed By Dreamon - Free Version | https://discord.gg/rokidmanager' + Style.RESET_ALL)

def detect_and_write_lua_script():
    detected_executors = []
    for executor_name, base_path in executors.items():
        possible_autoexec_paths = [os.path.join(base_path, 'Autoexec'), os.path.join(base_path, 'Autoexecute')]
        lua_written = False
        for path in possible_autoexec_paths:
            if os.path.exists(path):
                lua_script_path = os.path.join(path, 'executor_check.lua')
                try:
                    with open(lua_script_path, 'w') as file:
                        file.write(lua_script_template)
                    lua_written = True
                    break
                except Exception:
                    pass
        if lua_written:
            detected_executors.append(executor_name)
    return detected_executors

def capture_screenshot():
    screenshot_path = '/storage/emulated/0/Download/screenshot.png'
    try:
        os.system('{}{}'.format('/system/bin/screencap -p ', screenshot_path))
        print(Fore.GREEN + '{}{}'.format('[ Rokid Manager ] - Screenshot saved to: ', screenshot_path) + Style.RESET_ALL)
        return screenshot_path
    except Exception as e:
        print(Fore.RED + '{}{}'.format('[ Rokid Manager ] - Error capturing screenshot: ', e) + Style.RESET_ALL)
        return None

def get_system_info():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    uptime = time.time() - psutil.boot_time()
    system_info = {'cpu_usage': cpu_usage, 'memory_total': memory_info.total, 'memory_available': memory_info.available, 'memory_used': memory_info.used, 'uptime': uptime}
    return system_info

def load_config():
    global webhook_url, device_name, interval
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as file:
            config = json.load(file)
            webhook_url = config.get('webhook_url')
            device_name = config.get('device_name')
            interval = config.get('interval')
    else:
        webhook_url = None
        device_name = None
        interval = None

def save_config():
    config = {'webhook_url': webhook_url, 'device_name': device_name, 'interval': interval}
    with open(CONFIG_FILE, 'w') as file:
        json.dump(config, file)

def start_webhook_thread():
    global webhook_thread, stop_webhook_thread
    if webhook_thread is None or not webhook_thread.is_alive():
        stop_webhook_thread = False
        webhook_thread = threading.Thread(target=send_webhook)
        webhook_thread.start()

def send_webhook():
    global stop_webhook_thread
    while not stop_webhook_thread:
        screenshot_path = capture_screenshot()
        if screenshot_path is None:
            continue
        if not os.path.exists(screenshot_path):
            print(Fore.RED + (lambda: (lambda: (lambda: h2o(list(map(o2, ['[', ' ', 'R', 'o', 'k', 'i', 'd', ' ', 'M', 'a', 'n', 'a', 'g', 'e', 'r', ' ', ']', ' ', '-', ' ', 'S', 'c', 'r', 'e', 'e', 'n', 's', 'h', 'o', 't', ' ', 'f', 'i', 'l', 'e', ' ', 'd', 'o', 'e', 's', ' ', 'n', 'o', 't', ' ', 'e', 'x', 'i', 's', 't', '.']))))())())() + Style.RESET_ALL)
            continue
        system_info = get_system_info()
        embed = {'color': '蘂', 'fields': [{'name': ':small_blue_diamond: Device Name', 'value': '{}{}{}'.format('`', device_name, '`'), 'inline': True}, {'name': ':gear: CPU Usage', 'value': '{}{}{}'.format('`', system_info['cpu_usage'], '%`'), 'inline': True}, {'name': ':floppy_disk: Memory Usage', 'value': '{}{}{}'.format('`', system_info['memory_used'] / system_info['memory_total'] * 100, '%`'), 'inline': True}, {'name': ':floppy_disk: Memory Available', 'value': '{}{}{}'.format('`', system_info['memory_available'] / system_info['memory_total'] * 100, '%`'), 'inline': True}, {'name': ':bulb: Total Memory', 'value': '{}{}{}'.format('`', system_info['memory_total'] / 1024 ** 3, ' GB`'), 'inline': True}, {'name': ':timer: Uptime', 'value': '{}{}{}'.format('`', system_info['uptime'] / 3600, ' hours`'), 'inline': True}], 'image': {'url': 'attachment://screenshot.png'}, 'footer': {'text': 'discord.gg/rokidmanager', 'icon_url': 'https://images-ext-1.discordapp.net/external/J_N9HjmqaSHjVLUKVZiw-637-Aqw6NnlGSgwn44JnVU/%3Fsize%3D4096/https/cdn.discordapp.com/icons/1283014545513906278/5d85563d6b5c6d7b2a891fd673fad789.png?format=webp&quality=lossless'}, 'author': {'name': 'Rokid Manager', 'icon_url': 'https://images-ext-1.discordapp.net/external/J_N9HjmqaSHjVLUKVZiw-637-Aqw6NnlGSgwn44JnVU/%3Fsize%3D4096/https/cdn.discordapp.com/icons/1283014545513906278/5d85563d6b5c6d7b2a891fd673fad789.png?format=webp&quality=lossless'}}
        payload = {'embeds': [embed], 'username': device_name}
        with open(screenshot_path, 'rb') as file:
            response = requests.post(webhook_url, data={'payload_json': json.dumps(payload)}, files={'file': ('screenshot.png', file)})
        if response.status_code == 204 or response.status_code == 200:
            print(Fore.GREEN + (lambda: (lambda: (lambda: h2o(list(map(o2, ['[', ' ', 'R', 'o', 'k', 'i', 'd', ' ', 'M', 'a', 'n', 'a', 'g', 'e', 'r', ' ', ']', ' ', '-', ' ', 'D', 'e', 'v', 'i', 'c', 'e', ' ', 'i', 'n', 'f', 'o', 'r', 'm', 'a', 't', 'i', 'o', 'n', ' ', 'h', 'a', 's', ' ', 'b', 'e', 'e', 'n', ' ', 's', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l', 'l', 'y', ' ', 's', 'e', 'n', 't', ' ', 't', 'o', ' ', 't', 'h', 'e', ' ', 'w', 'e', 'b', 'h', 'o', 'o', 'k', '.']))))())())() + Style.RESET_ALL)
        else:
            print(Fore.RED + '{}{}'.format('[ Rokid Manager ] - Error sending device information to the webhook, status code: ', response.status_code) + Style.RESET_ALL)
        time.sleep(interval * 60)

def stop_webhook():
    global stop_webhook_thread
    stop_webhook_thread = True

def setup_webhook():
    global webhook_url, device_name, interval, stop_webhook_thread
    stop_webhook_thread = True
    webhook_url = safe_input(Fore.MAGENTA + (lambda: (lambda: (lambda: h2o(list(map(o2, ['[', ' ', 'R', 'o', 'k', 'i', 'd', ' ', 'M', 'a', 'n', 'a', 'g', 'e', 'r', ' ', ']', ' ', '-', ' ', 'P', 'l', 'e', 'a', 's', 'e', ' ', 'e', 'n', 't', 'e', 'r', ' ', 'y', 'o', 'u', 'r', ' ', 'W', 'e', 'b', 'h', 'o', 'o', 'k', ' ', 'U', 'R', 'L', ':', ' ']))))())())() + Style.RESET_ALL)
    device_name = safe_input(Fore.MAGENTA + (lambda: (lambda: (lambda: h2o(list(map(o2, ['[', ' ', 'R', 'o', 'k', 'i', 'd', ' ', 'M', 'a', 'n', 'a', 'g', 'e', 'r', ' ', ']', ' ', '-', ' ', 'P', 'l', 'e', 'a', 's', 'e', ' ', 'e', 'n', 't', 'e', 'r', ' ', 'y', 'o', 'u', 'r', ' ', 'd', 'e', 'v', 'i', 'c', 'e', ' ', 'n', 'a', 'm', 'e', ':', ' ']))))())())() + Style.RESET_ALL)
    interval = int(safe_input(Fore.MAGENTA + (lambda: (lambda: (lambda: h2o(list(map(o2, ['[', ' ', 'R', 'o', 'k', 'i', 'd', ' ', 'M', 'a', 'n', 'a', 'g', 'e', 'r', ' ', ']', ' ', '-', ' ', 'P', 'l', 'e', 'a', 's', 'e', ' ', 'e', 'n', 't', 'e', 'r', ' ', 't', 'h', 'e', ' ', 'i', 'n', 't', 'e', 'r', 'v', 'a', 'l', ' ', 't', 'o', ' ', 's', 'e', 'n', 'd', ' ', 'd', 'e', 'v', 'i', 'c', 'e', ' ', 'i', 'n', 'f', 'o', 'r', 'm', 'a', 't', 'i', 'o', 'n', ' ', 't', 'o', ' ', 't', 'h', 'e', ' ', 'W', 'e', 'b', 'h', 'o', 'o', 'k', ' ', (lambda: c2h6(b"Dreamon/\xffy'"))(), 'i', 'n', ' ', 'm', 'i', 'n', 'u', 't', 'e', 's', ')', ':', ' ']))))())())() + Style.RESET_ALL))
    save_config()
    stop_webhook_thread = False
    threading.Thread(target=send_webhook).start()

def reset_executor_file(username):
    status_file = '{}{}{}'.format('executor_check_', username, '.txt')
    valid_workspace = None
    for executor, base_path in executors.items():
        for workspace_dir in ['workspace', 'Workspace']:
            workspace_path = os.path.join(base_path, workspace_dir)
            if os.path.exists(workspace_path):
                valid_workspace = workspace_path
                break
        if valid_workspace:
            file_path = os.path.join(valid_workspace, status_file)
            if os.path.exists(file_path):
                try:
                    os.remove(file_path)
                except Exception as e:
                    pass
            break

def clear_executor_status(username):
    status_file = '{}{}{}'.format('executor_check_', username, '.txt')
    valid_workspace = None
    for executor, base_path in executors.items():
        for workspace_dir in ['workspace', 'Workspace']:
            workspace_path = os.path.join(base_path, workspace_dir)
            if os.path.exists(workspace_path):
                valid_workspace = workspace_path
                break
        if valid_workspace:
            file_path = os.path.join(valid_workspace, status_file)
            if os.path.exists(file_path):
                try:
                    os.remove(file_path)
                except Exception as e:
                    pass
            break

def check_executor_status(username, continuous=False, max_wait_time=230, check_interval=4, max_inactivity_time=30):
    status_file = '{}{}{}'.format('executor_check_', username, '.txt')
    retry_timeout = time.time() + max_wait_time
    active_workspace = None
    for executor, base_path in executors.items():
        for workspace_dir in ['workspace', 'Workspace']:
            workspace_path = os.path.join(base_path, workspace_dir)
            if os.path.exists(workspace_path):
                active_workspace = workspace_path
                break
        if active_workspace:
            break
    if not active_workspace:
        return True
    start_time = time.time()
    while True:
        file_path = os.path.join(active_workspace, status_file)
        if os.path.exists(file_path):
            last_modified_time = os.path.getmtime(file_path)
            current_time = time.time()
            if current_time - last_modified_time < max_inactivity_time:
                with open(file_path, 'r') as f:
                    content = f.read().strip()
                    if content.startswith('working'):
                        return True
        if not continuous and time.time() > retry_timeout:
            return False
        time.sleep(check_interval)

def create_dynamic_menu(options):
    clear_console()
    print_header()
    table = PrettyTable()
    table.field_names = ['Option', 'Function']
    table.align = 'l'
    table.border = True
    for i, option in enumerate(options, start=1):
        table.add_row(['{}{}'.format(i, '.'), option])
    print(Fore.LIGHTCYAN_EX + str(table))

def create_dynamic_table(headers, rows):
    clear_console()
    print_header()
    table = PrettyTable()
    table.field_names = headers
    table.align = 'l'
    table.border = True
    for row in rows:
        table.add_row(row)
    print(str(table))

def handle_exit_signal(signum, frame):
    print(Fore.YELLOW + (lambda: (lambda: (lambda: h2o(list(map(o2, ['[', ' ', 'R', 'o', 'k', 'i', 'd', ' ', 'M', 'a', 'n', 'a', 'g', 'e', 'r', ' ', ']', ' ', '-', '>', ' ', 'S', 'h', 'u', 't', 't', 'i', 'n', 'g', ' ', 'd', 'o', 'w', 'n', ' ', 'g', 'r', 'a', 'c', 'e', 'f', 'u', 'l', 'l', 'y', '.', '.', '.']))))())())() + Style.RESET_ALL)
    print(Fore.LIGHTMAGENTA_EX + (lambda: (lambda: (lambda: h2o(list(map(o2, ['[', ' ', 'R', 'o', 'k', 'i', 'd', ' ', 'M', 'a', 'n', 'a', 'g', 'e', 'r', ' ', ']', ' ', '-', '>', ' ', 'C', 'a', 'c', 'h', 'e', ' ', 's', 'a', 'v', 'e', 'd', ' ', 'a', 'n', 'd', ' ', 't', 'h', 'r', 'e', 'a', 'd', 's', ' ', 's', 't', 'o', 'p', 'p', 'e', 'd', '.']))))())())())

def update_status_table(package_statuses):
    clear_console()
    print_header()
    table = PrettyTable()
    table.field_names = ['Package', 'Username', 'Status']
    table.align = 'l'
    table.border = True
    for package, info in package_statuses.items():
        table.add_row([package, info.get('Username', 'Unknown'), info.get('Status', '')])
    print(str(table))

def verify_cookie(cookie_value):
    try:
        headers = {'Cookie': '{}{}'.format('.ROBLOSECURITY=', cookie_value), 'User-Agent': 'Mozilla/5.0 Linux; Android 10; Mobile) AppleWebKit/537.36 KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36', 'Referer': 'https://www.roblox.com/', 'Origin': 'https://www.roblox.com', 'Accept-Language': 'en-US,en;q=0.9', 'Accept-Encoding': 'gzip, deflate, br', 'Connection': 'keep-alive'}
        time.sleep(0)
        response = requests.get('https://users.roblox.com/v1/users/authenticated', headers=headers)
        if response.status_code == 200:
            print(Fore.GREEN + (lambda: (lambda: (lambda: h2o(list(map(o2, ['[', ' ', 'R', 'o', 'k', 'i', 'd', ' ', 'M', 'a', 'n', 'a', 'g', 'e', 'r', ' ', ']', ' ', '-', '>', ' ', 'C', 'o', 'o', 'k', 'i', 'e', ' ', 'i', 's', ' ', 'v', 'a', 'l', 'i', 'd', '!', ' ', 'U', 's', 'e', 'r', ' ', 'i', 's', ' ', 'a', 'u', 't', 'h', 'e', 'n', 't', 'i', 'c', 'a', 't', 'e', 'd', '.']))))())())() + Style.RESET_ALL)
            return True
        elif response.status_code == 401:
            print(Fore.RED + (lambda: (lambda: (lambda: h2o(list(map(o2, ['[', ' ', 'R', 'o', 'k', 'i', 'd', ' ', 'M', 'a', 'n', 'a', 'g', 'e', 'r', ' ', ']', ' ', '-', '>', ' ', 'I', 'n', 'v', 'a', 'l', 'i', 'd', ' ', 'c', 'o', 'o', 'k', 'i', 'e', '.', ' ', 'T', 'h', 'e', ' ', 'u', 's', 'e', 'r', ' ', 'i', 's', ' ', 'n', 'o', 't', ' ', 'a', 'u', 't', 'h', 'e', 'n', 't', 'i', 'c', 'a', 't', 'e', 'd', '.']))))())())() + Style.RESET_ALL)
            return False
        else:
            print(Fore.RED + '{}{}{}{}'.format('[ Rokid Manager ] -> Error verifying cookie: ', response.status_code, ' - ', response.text) + Style.RESET_ALL)
            return False
    except Exception as e:
        print(Fore.RED + '{}{}'.format('Exception occurred while verifying cookie: ', e) + Style.RESET_ALL)
        return False

def download_file(url, destination, binary=False):
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            mode = 'wb' if binary else 'w'
            with open(destination, mode) as file:
                if binary:
                    shutil.copyfileobj(response.raw, file)
                else:
                    file.write(response.text)
            print(Fore.GREEN + '{}{}{}'.format('[ Rokid Manager ] -> ', os.path.basename(destination), ' downloaded successfully.') + Style.RESET_ALL)
            return destination
        else:
            print(Fore.RED + '{}{}{}'.format('[ Rokid Manager ] -> Failed to download ', os.path.basename(destination), '.') + Style.RESET_ALL)
            return None
    except Exception as e:
        print(Fore.RED + '{}{}{}{}'.format('[ Rokid Manager ] -> Error downloading ', os.path.basename(destination), ': ', e) + Style.RESET_ALL)
        return None

def replace_cookie_value_in_db(db_path, new_cookie_value):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute('            SELECT COUNT*) FROM cookies WHERE host_key = .roblox.com AND name = .ROBLOSECURITY        ')
        cookie_exists = cursor.fetchone()[0]
        if cookie_exists:
            cursor.execute('                UPDATE cookies                SET value = ?, last_access_utc = ?, expires_utc = ?                WHERE host_key = .roblox.com AND name = .ROBLOSECURITY            ', (new_cookie_value, int(time.time() * 1000000), 99999999999999999))
        else:
            cursor.execute('                INSERT INTO cookies creation_utc, host_key, name, value, path, expires_utc, is_secure, is_httponly, last_access_utc)                VALUES ?, .roblox.com, .ROBLOSECURITY, ?, /, 99999999999999999, 0, 0, ?)            ', (int(time.time() * 1000000), new_cookie_value, int(time.time() * 1000000)))
        conn.commit()
        conn.close()
        print(Fore.GREEN + (lambda: (lambda: (lambda: h2o(list(map(o2, ['[', ' ', 'R', 'o', 'k', 'i', 'd', ' ', 'M', 'a', 'n', 'a', 'g', 'e', 'r', ' ', ']', ' ', '-', '>', ' ', 'C', 'o', 'o', 'k', 'i', 'e', ' ', 'v', 'a', 'l', 'u', 'e', ' ', 'r', 'e', 'p', 'l', 'a', 'c', 'e', 'd', ' ', 's', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l', 'l', 'y', ' ', 'i', 'n', ' ', 't', 'h', 'e', ' ', 'd', 'a', 't', 'a', 'b', 'a', 's', 'e', '!']))))())())() + Style.RESET_ALL)
    except sqlite3.OperationalError as e:
        print(Fore.RED + '{}{}'.format('[ Rokid Manager ] -> Database error during cookie replacement: ', e) + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + '{}{}'.format('[ Rokid Manager ] -> Error replacing cookie value in database: ', e) + Style.RESET_ALL)

def inject_cookies_and_appstorage():
    db_url = 'https://github.com/thieusitinks/Rokid-Manager/raw/refs/heads/main/Cookies'
    appstorage_url = 'https://raw.githubusercontent.com/thieusitinks/Rokid-Manager/refs/heads/main/appStorage.json'
    downloaded_db_path = download_file(db_url, 'Cookies.db', binary=True)
    downloaded_appstorage_path = download_file(appstorage_url, 'appStorage.json', binary=False)
    if not downloaded_db_path or not downloaded_appstorage_path:
        print(Fore.RED + (lambda: (lambda: (lambda: h2o(list(map(o2, ['[', ' ', 'R', 'o', 'k', 'i', 'd', ' ', 'M', 'a', 'n', 'a', 'g', 'e', 'r', ' ', ']', ' ', '-', '>', ' ', 'F', 'a', 'i', 'l', 'e', 'd', ' ', 't', 'o', ' ', 'd', 'o', 'w', 'n', 'l', 'o', 'a', 'd', ' ', 'n', 'e', 'c', 'e', 's', 's', 'a', 'r', 'y', ' ', 'f', 'i', 'l', 'e', 's', '.', ' ', 'E', 'x', 'i', 't', 'i', 'n', 'g', '.']))))())())() + Style.RESET_ALL)
        return
    cookie_txt_path = 'cookie.txt'
    if not os.path.exists(cookie_txt_path):
        print(Fore.RED + (lambda: (lambda: (lambda: h2o(list(map(o2, ['[', ' ', 'R', 'o', 'k', 'i', 'd', ' ', 'M', 'a', 'n', 'a', 'g', 'e', 'r', ' ', ']', ' ', '-', '>', ' ', 'c', 'o', 'o', 'k', 'i', 'e', '.', 't', 'x', 't', ' ', 'n', 'o', 't', ' ', 'f', 'o', 'u', 'n', 'd', ' ', 'i', 'n', ' ', 't', 'h', 'e', ' ', 'c', 'u', 'r', 'r', 'e', 'n', 't', ' ', 'd', 'i', 'r', 'e', 'c', 't', 'o', 'r', 'y', '!']))))())())() + Style.RESET_ALL)
        with open(cookie_txt_path, 'w') as file:
            file.write('')
        print(Fore.GREEN + (lambda: (lambda: (lambda: h2o(list(map(o2, ['[', ' ', 'R', 'o', 'k', 'i', 'd', ' ', 'M', 'a', 'n', 'a', 'g', 'e', 'r', ' ', ']', ' ', '-', '>', ' ', 'c', 'o', 'o', 'k', 'i', 'e', '.', 't', 'x', 't', ' ', 'h', 'a', 's', ' ', 'b', 'e', 'e', 'n', ' ', 'c', 'r', 'e', 'a', 't', 'e', 'd', ' ', '!']))))())())() + Style.RESET_ALL)
        return
    with open(cookie_txt_path, 'r') as file:
        cookies = [line.strip() for line in file.readlines()]
    if not cookies:
        print(Fore.RED + (lambda: (lambda: (lambda: h2o(list(map(o2, ['[', ' ', 'R', 'o', 'k', 'i', 'd', ' ', 'M', 'a', 'n', 'a', 'g', 'e', 'r', ' ', ']', ' ', '-', '>', ' ', 'N', 'o', ' ', 'c', 'o', 'o', 'k', 'i', 'e', 's', ' ', 'f', 'o', 'u', 'n', 'd', ' ', 'i', 'n', ' ', 'c', 'o', 'o', 'k', 'i', 'e', '.', 't', 'x', 't', '.', ' ', 'P', 'l', 'e', 'a', 's', 'e', ' ', 'a', 'd', 'd', ' ', 'y', 'o', 'u', 'r', ' ', 'c', 'o', 'o', 'k', 'i', 'e', 's', '.']))))())())() + Style.RESET_ALL)
        return
    packages = get_roblox_packages()
    if len(cookies) > len(packages):
        print(Fore.RED + (lambda: (lambda: (lambda: h2o(list(map(o2, ['[', ' ', 'R', 'o', 'k', 'i', 'd', ' ', 'M', 'a', 'n', 'a', 'g', 'e', 'r', ' ', ']', ' ', '-', '>', ' ', 'M', 'o', 'r', 'e', ' ', 'c', 'o', 'o', 'k', 'i', 'e', 's', ' ', 'i', 'n', ' ', 'c', 'o', 'o', 'k', 'i', 'e', '.', 't', 'x', 't', ' ', 't', 'h', 'a', 'n', ' ', 'p', 'a', 'c', 'k', 'a', 'g', 'e', 's', ' ', 'a', 'v', 'a', 'i', 'l', 'a', 'b', 'l', 'e', '.', ' ', 'E', 'n', 's', 'u', 'r', 'e', ' ', 'e', 'a', 'c', 'h', ' ', 'c', 'o', 'o', 'k', 'i', 'e', ' ', 'h', 'a', 's', ' ', 'a', ' ', 'c', 'o', 'r', 'r', 'e', 's', 'p', 'o', 'n', 'd', 'i', 'n', 'g', ' ', 'p', 'a', 'c', 'k', 'a', 'g', 'e', '.']))))())())() + Style.RESET_ALL)
        return
    for idx, package_name in enumerate(packages):
        try:
            raw_cookie = cookies[idx]
            cookie = None
            username, password = (None, None)
            if raw_cookie.count(':') >= 2:
                parts = raw_cookie.split(':')
                username = parts[0]
                password = parts[1]
                cookie = ':'.join(parts[2:])
            else:
                cookie = cookies[idx]
            print(Fore.CYAN + '{}{}{}'.format('[ Rokid Manager ] -> Verifying cookie for ', package_name, ' before injection...') + Style.RESET_ALL)
            if verify_cookie(cookie):
                print(Fore.GREEN + '{}{}{}'.format('[ Rokid Manager ] -> Cookie for ', package_name, ' is valid!') + Style.RESET_ALL)
            else:
                print(Fore.RED + '{}{}{}'.format('[ Rokid Manager ] -> Cookie for ', package_name, ' is invalid. Skipping injection...') + Style.RESET_ALL)
                continue
            print(Fore.GREEN + '{}{}{}{}'.format('[ Rokid Manager ] -> Injecting cookie for ', package_name, ': ', cookie) + Style.RESET_ALL)
            destination_db_dir = '{}{}{}'.format('/data/data/', package_name, '/app_webview/Default/')
            destination_appstorage_dir = '{}{}{}'.format('/data/data/', package_name, '/files/appData/LocalStorage/')
            os.makedirs(destination_db_dir, exist_ok=True)
            os.makedirs(destination_appstorage_dir, exist_ok=True)
            destination_db_path = os.path.join(destination_db_dir, 'Cookies')
            shutil.copyfile(downloaded_db_path, destination_db_path)
            print(Fore.GREEN + '{}{}'.format('Copied Cookies.db to ', destination_db_path) + Style.RESET_ALL)
            destination_appstorage_path = os.path.join(destination_appstorage_dir, 'appStorage.json')
            shutil.copyfile(downloaded_appstorage_path, destination_appstorage_path)
            print(Fore.GREEN + '{}{}'.format('Copied appStorage.json to ', destination_appstorage_path) + Style.RESET_ALL)
            replace_cookie_value_in_db(destination_db_path, cookie)
            print(Fore.CYAN + '{}{}{}'.format('[ Rokid Manager ] -> Verifying cookie for ', package_name, ' after injection...') + Style.RESET_ALL)
            if verify_cookie(cookie):
                print(Fore.GREEN + '{}{}{}'.format('Cookie for ', package_name, ' is valid after injection!') + Style.RESET_ALL)
            else:
                print(Fore.RED + '{}{}{}'.format('Cookie for ', package_name, ' is invalid after injection!') + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + '{}{}{}{}'.format('Error injecting cookie for ', package_name, ': ', e) + Style.RESET_ALL)
    print(Fore.GREEN + (lambda: (lambda: (lambda: h2o(list(map(o2, ['[', ' ', 'R', 'o', 'k', 'i', 'd', ' ', 'M', 'a', 'n', 'a', 'g', 'e', 'r', ' ', ']', ' ', '-', '>', ' ', 'C', 'o', 'o', 'k', 'i', 'e', ' ', 'a', 'n', 'd', ' ', 'a', 'p', 'p', 'S', 't', 'o', 'r', 'a', 'g', 'e', ' ', 'i', 'n', 'j', 'e', 'c', 't', 'i', 'o', 'n', ' ', 'c', 'o', 'm', 'p', 'l', 'e', 't', 'e', 'd', ' ', 'f', 'o', 'r', ' ', 'a', 'l', 'l', ' ', 'p', 'a', 'c', 'k', 'a', 'g', 'e', 's', '.']))))())())() + Style.RESET_ALL)

def get_roblox_packages():
    packages = []
    try:
        output = subprocess.check_output('pm list packages', shell=True, text=True)
    except subprocess.CalledProcessError:
        print(Fore.RED + 'An error occurred while searching for packages on your device!' + Style.RESET_ALL)
        return packages
    print(Fore.YELLOW + 'Checking Packages On Your Device .....' + Style.RESET_ALL)
    for line in output.splitlines():
        if 'com.roblox.' in line:
            package_name = line.split(':')[1]
            print(Fore.GREEN + '{}{}'.format('Package Found : ', package_name) + Style.RESET_ALL)
            packages.append(package_name)
    if not packages:
        print(Fore.RED + 'No Roblox-related packages found on your device.' + Style.RESET_ALL)
    return packages

def is_roblox_running(package_name):
    for proc in psutil.process_iter(['name']):
        if package_name in proc.info['name'].lower():
            return True
    return False

def kill_roblox_processes():
    print('Killing all Roblox processes...')
    package_names = get_roblox_packages()
    for package_name in package_names:
        print('{}{}'.format('Trying to kill process for package: ', package_name))
        os.system('{}{}'.format('pkill -f ', package_name))
    time.sleep(2)

def kill_roblox_process(package_name):
    print('{}{}{}'.format('Killing Roblox process for ', package_name, '...'))
    os.system('{}{}'.format('pkill -f ', package_name))
    time.sleep(2)

def launch_roblox(package_name, server_link, num_packages, package_statuses):
    try:
        package_statuses[package_name]['Status'] = Fore.LIGHTCYAN_EX + '{}{}{}'.format('Opening Roblox for ', package_name, '...') + Style.RESET_ALL
        update_status_table(package_statuses)
        subprocess.run(['am', 'start', '-n', '{}{}'.format(package_name, '/com.roblox.client.startup.ActivitySplash'), '-d', server_link], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(15 if num_packages >= 6 else 8)
        package_statuses[package_name]['Status'] = Fore.LIGHTCYAN_EX + '{}{}{}'.format('Joining Roblox for ', package_name, '...') + Style.RESET_ALL
        update_status_table(package_statuses)
        subprocess.run(['am', 'start', '-n', '{}{}'.format(package_name, '/com.roblox.client.ActivityProtocolLaunch'), '-d', server_link], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(20)
        package_statuses[package_name]['Status'] = Fore.GREEN + 'Joined Roblox' + Style.RESET_ALL
        update_status_table(package_statuses)
    except Exception as e:
        package_statuses[package_name]['Status'] = Fore.RED + '{}{}{}{}'.format('Error launching Roblox for ', package_name, ': ', e) + Style.RESET_ALL
        update_status_table(package_statuses)
        print('{}{}'.format('Error details: ', e))

def check_executor_and_rejoin(package_name, username, package_statuses, server_link, num_packages, accounts):
    try:
        detected_executors = detect_and_write_lua_script()
        if detected_executors:
            print('{}{}{}{}{}'.format('Checking executor status for ', package_name, ' with username ', username, '...'))
            start_time = time.time()
            executor_loaded = False
            while time.time() - start_time < 60:
                if check_executor_status(username):
                    package_statuses[package_name]['Status'] = Fore.GREEN + '{}{}'.format('Executor loaded successfully for ', username) + Style.RESET_ALL
                    executor_loaded = True
                    break
                time.sleep(10)
            if not executor_loaded:
                print('{}{}{}{}{}'.format('Executor did not load for ', package_name, ' (username: ', username, '). Rejoining...'))
                package_statuses[package_name]['Status'] = Fore.RED + 'Executor failed, rejoining...' + Style.RESET_ALL
                update_status_table(package_statuses)
                kill_roblox_process(package_name)
                time.sleep(2)
                launch_roblox(package_name, server_link, num_packages, package_statuses)
                check_executor_and_rejoin(package_name, username, package_statuses, server_link, num_packages, accounts)
        else:
            print('{}{}{}{}{}'.format('No executor detected for ', package_name, ' (username: ', username, ').'))
            package_statuses[package_name]['Status'] = Fore.GREEN + '{}{}'.format('Joined without executor for ', username) + Style.RESET_ALL
            update_status_table(package_statuses)
        monitor_thread = threading.Thread(target=background_executor_monitor, args=(package_name, username, package_statuses, server_link, num_packages))
        monitor_thread.daemon = True
        monitor_thread.start()
    except Exception as e:
        package_statuses[package_name]['Status'] = Fore.RED + '{}{}{}{}'.format('Error checking executor for ', package_name, ': ', e) + Style.RESET_ALL
        update_status_table(package_statuses)

def background_executor_monitor(package_name, username, package_statuses, server_link, num_packages, retry_limit=3):
    retry_count = 0
    try:
        while True:
            if not check_executor_status(username, continuous=False):
                retry_count += 1
                package_statuses[package_name]['Status'] = Fore.RED + 'Executor failed, rejoining...' + Style.RESET_ALL
                update_status_table(package_statuses)
                if retry_count >= retry_limit:
                    package_statuses[package_name]['Status'] = Fore.RED + 'Reached retry limit, stopping rejoin attempts...' + Style.RESET_ALL
                    update_status_table(package_statuses)
                    break
                with rejoin_lock:
                    kill_roblox_process(package_name)
                    time.sleep(5)
                    launch_roblox(package_name, server_link, num_packages, package_statuses)
                    time.sleep(120)
                if check_executor_status(username, continuous=False):
                    retry_count = 0
                    package_statuses[package_name]['Status'] = Fore.GREEN + 'Executor reloaded successfully after rejoin.' + Style.RESET_ALL
                    update_status_table(package_statuses)
                else:
                    package_statuses[package_name]['Status'] = Fore.RED + 'Executor still failed after rejoin, retrying...' + Style.RESET_ALL
                    update_status_table(package_statuses)
            time.sleep(30)
    except Exception as e:
        package_statuses[package_name]['Status'] = Fore.RED + '{}{}'.format('Error in background monitor: ', e) + Style.RESET_ALL
        update_status_table(package_statuses)

def get_game_name(game_link_or_id):
    try:
        if 'roblox.com' in game_link_or_id:
            game_id = game_link_or_id.split('/')[-1]
        else:
            game_id = game_link_or_id
        url = '{}{}'.format('https://games.roblox.com/v1/games?universeIds=', game_id)
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            game_data = response.json()
            if game_data['data']:
                return game_data['data'][0]['name']
            else:
                return 'Unknown Game'
        else:
            return 'Failed to retrieve game name'
    except Exception as e:
        print(Fore.RED + '{}{}'.format('Error retrieving game name: ', e) + Style.RESET_ALL)
        return 'Error'

def format_server_link(input_link):
    if 'roblox.com' in input_link:
        return input_link
    elif input_link.isdigit():
        return '{}{}'.format('roblox://placeID=', input_link)
    else:
        print(Fore.RED + 'Invalid input! Please enter a valid game ID or private server link.' + Style.RESET_ALL)
        return None

def save_server_links(server_links):
    with open(SERVER_LINKS_FILE, 'w') as file:
        for package, link in server_links:
            file.write('{}{}{}{}'.format(package, ',', link, '\n'))

def load_server_links():
    server_links = []
    if os.path.exists(SERVER_LINKS_FILE):
        with open(SERVER_LINKS_FILE, 'r') as file:
            for line in file:
                package, link = line.strip().split(',', 1)
                server_links.append((package, link))
    return server_links

def save_accounts(accounts):
    with open(ACCOUNTS_FILE, 'w') as file:
        for package, user_id in accounts:
            file.write('{}{}{}{}'.format(package, ',', user_id, '\n'))

def load_accounts():
    accounts = []
    if os.path.exists(ACCOUNTS_FILE):
        with open(ACCOUNTS_FILE, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    try:
                        package, user_id = line.split(',', 1)
                        accounts.append((package, user_id))
                    except ValueError:
                        print('{}{}{}{}{}'.format(Fore.RED, 'Invalid line format: ', line, ". Expected format 'package,user_id'.", Style.RESET_ALL))
    return accounts

def find_userid_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            userid_start = content.find('"UserId":"')
            if userid_start == -1:
                print('Userid not found')
                return None
            userid_start += len('"UserId":"')
            userid_end = content.find('"', userid_start)
            if userid_end == -1:
                print('Userid end quote not found')
                return None
            userid = content[userid_start:userid_end]
            return userid
    except IOError as e:
        print('{}{}'.format('Error reading file: ', e))
        return None

async def get_user_id(username):
    url = 'https://users.roblox.com/v1/usernames/users'
    payload = {'usernames': [username], 'excludeBannedUsers': True}
    headers = {'Content-Type': 'application/json'}
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload, headers=headers) as response:
            data = await response.json()
            if 'data' in data and len(data['data']) > 0:
                return data['data'][0]['id']
    return None

def get_server_link(package_name, server_links):
    return next((link for pkg, link in server_links if pkg == package_name), None)

def get_username_from_id(user_id):
    return get_username(user_id) or user_id

def get_username(user_id):
    retry_attempts = 2
    for attempt in range(retry_attempts):
        try:
            url = '{}{}'.format('https://users.roblox.com/v1/users/', user_id)
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            username = data.get('name', 'Unknown')
            if username != 'Unknown':
                username_cache[user_id] = username
                save_username(user_id, username)
                return username
        except requests.exceptions.RequestException as e:
            print(Fore.RED + '{}{}{}{}'.format('Attempt ', attempt + 1, ' failed for Roblox Users API: ', e) + Style.RESET_ALL)
            time.sleep(2 ** attempt)
    for attempt in range(retry_attempts):
        try:
            url = '{}{}'.format('https://users.roproxy.com/v1/users/', user_id)
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            username = data.get('name', 'Unknown')
            if username != 'Unknown':
                username_cache[user_id] = username
                save_username(user_id, username)
                return username
        except requests.exceptions.RequestException as e:
            print(Fore.RED + '{}{}{}{}'.format('Attempt ', attempt + 1, ' failed for RoProxy API: ', e) + Style.RESET_ALL)
            time.sleep(2 ** attempt)
    return 'Unknown'

def save_username(user_id, username):
    try:
        if not os.path.exists('usernames.json'):
            with open('usernames.json', 'w') as file:
                json.dump({user_id: username}, file)
        else:
            with open('usernames.json', 'r+') as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = {}
                data[user_id] = username
                file.seek(0)
                json.dump(data, file)
                file.truncate()
    except (IOError, json.JSONDecodeError) as e:
        print(Fore.RED + '{}{}'.format('Error saving username: ', e) + Style.RESET_ALL)

def load_saved_username(user_id):
    try:
        with open('usernames.json', 'r') as file:
            data = json.load(file)
            return data.get(user_id)
    except (FileNotFoundError, json.JSONDecodeError, IOError) as e:
        print(Fore.RED + '{}{}'.format('Error loading username: ', e) + Style.RESET_ALL)
        return None

def load_cache():
    global username_cache
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'r') as f:
            username_cache = json.load(f)

def save_cache():
    try:
        temp_file = CACHE_FILE + '.tmp'
        with open(temp_file, 'w') as f:
            json.dump(username_cache, f)
        os.replace(temp_file, CACHE_FILE)
    except IOError as e:
        print(Fore.RED + '{}{}'.format('Error saving cache: ', e) + Style.RESET_ALL)

def check_user_online(user_id):
    max_retries = 3
    delay = 2
    for attempt in range(max_retries):
        try:
            primary_url = 'https://presence.roblox.com/v1/presence/users'
            headers = {'Content-Type': 'application/json'}
            body = json.dumps({'userIds': [user_id]})
            with requests.Session() as session:
                primary_response = session.post(primary_url, headers=headers, data=body, timeout=7)
            primary_response.raise_for_status()
            primary_data = primary_response.json()
            primary_presence_type = primary_data['userPresences'][0]['userPresenceType']
            primary_last_location = primary_data['userPresences'][0].get('lastLocation', None)
            if primary_last_location == 'Website':
                print(Fore.YELLOW + '{}{}'.format(user_id, ' is currently on the Website. Rejoin recommended.') + Style.RESET_ALL)
                primary_presence_type = 0
            return (primary_presence_type, primary_last_location)
        except requests.exceptions.RequestException as e:
            print(Fore.RED + '{}{}{}{}{}{}'.format('Error checking online status for user ', user_id, ' (Attempt ', attempt + 1, '): ', e) + Style.RESET_ALL)
            if attempt < max_retries - 1:
                time.sleep(delay)
                delay *= 2
            else:
                return (None, None)

def get_hwid_file_path(package_name):
    directory = '{}{}{}'.format('/data/data/', package_name, '/app_assets/content/')
    try:
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        if not files:
            print(Fore.RED + 'No files found in the specified directory.' + Style.RESET_ALL)
            return None
        last_file = files[-1]
        hwid_file_path = os.path.join(directory, last_file)
        return hwid_file_path
    except Exception as e:
        print(Fore.RED + '{}{}'.format('Error retrieving HWID file path: ', e) + Style.RESET_ALL)
        return None

def get_hwid(package_name):
    directory = '{}{}{}'.format('/data/data/', package_name, '/app_assets/content/')
    try:
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        if not files:
            print(Fore.RED + 'No files found in the specified directory.' + Style.RESET_ALL)
            return None
        last_file = files[-1]
        hwid_file_path = os.path.join(directory, last_file)
        with open(hwid_file_path, 'r') as file:
            hwid = file.read().strip()
            print(Fore.GREEN + '{}{}'.format('HWID found: ', hwid) + Style.RESET_ALL)
            return hwid
    except Exception as e:
        print(Fore.RED + '{}{}'.format('Error retrieving HWID: ', e) + Style.RESET_ALL)
        return None

def get_hwid_platoboost():
    hwid = ''
    if os.path.exists('hwid_platoboost.txt'):
        with open('hwid_platoboost.txt', 'r') as f:
            hwid = f.read().strip()
            f.close()
    if hwid == '' or hwid == None:
        url = safe_input('Enter link platoboost you want to bypass: ')
        a = parse_qs(urlparse(url).query).get('id', [None])[0]
        if a is None:
            hwid = url
        else:
            hwid = a
        with open('hwid_platoboost.txt', 'w') as f:
            f.write(hwid)
            f.close()
    return hwid

def create_fluxus_bypass_link(hwid, api_key='XqzyaenZishd33axPYPz'):
    return '{}{}{}{}'.format('https://madkung.vercel.app/fluxus-api?url=https://flux.li/android/external/start.php?HWID=', hwid, '&api_key=', api_key)

def create_bypass_link(api, hwid):
    head_option = {'Host': 'api-gateway.platoboost.com', 'accept': '*/*', 'access-control-request-method': 'GET', 'access-control-request-headers': 'version', 'origin': 'https://gateway.platoboost.com', 'user-agent': 'Mozilla/5.0 Linux; Android 10; K) AppleWebKit/537.36 KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-site', 'sec-fetch-dest': 'empty', 'referer': 'https://gateway.platoboost.com/', 'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5', 'priority': 'u=1, i'}
    header = {'Host': 'api-gateway.platoboost.com', 'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"', 'accept': 'application/json', 'content-type': 'application/json', 'sec-ch-ua-platform': '"Android"', 'dnt': '1', 'sec-ch-ua-mobile': '?1', 'user-agent': 'Mozilla/5.0 Linux; Android 10; K) AppleWebKit/537.36 KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36', 'version': '3.3.5', 'origin': 'https://gateway.platoboost.com', 'sec-fetch-site': 'same-site', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty', 'referer': 'https://gateway.platoboost.com/', 'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5', 'priority': 'u=1, i'}
    session = requests.Session()
    data = {'captcha': '', 'type': ''}
    try:
        session.options('{}{}{}{}'.format('https://api-gateway.platoboost.com/v1/authenticators/', api, '/', hwid), headers=head_option, timeout=5)
        rokid_manager = session.get('{}{}{}{}'.format('https://api-gateway.platoboost.com/v1/authenticators/', api, '/', hwid), headers=header, timeout=5).json()
        if rokid_manager.get('key', False):
            t = rokid_manager.get('minutesLeft', 0)
            return {'key': rokid_manager.get('key'), 'timeleft': t * 60}
        checkpointCount = rokid_manager.get('checkpointCount', 0)
        captcha = rokid_manager.get('captcha', False)
        if captcha:
            return {'error': 'Cant bypass human security check!'}
        head_option['access-control-request-method'] = 'POST'
        head_option['access-control-request-headers'] = 'content-type,version'
        session.options('{}{}{}{}'.format('https://api-gateway.platoboost.com/v1/sessions/auth/', api, '/', hwid), headers=head_option, timeout=5)
        rokid_manager = session.post('{}{}{}{}'.format('https://api-gateway.platoboost.com/v1/sessions/auth/', api, '/', hwid), headers=header, json=data, timeout=5).json()
        for i in range(checkpointCount):
            if rokid_manager.get('redirect', False):
                r = parse_qs(urlparse(rokid_manager.get('redirect')).query)['r'][0]
                url = str(base64.b64decode(r).decode('utf-8'))
                tk = parse_qs(urlparse(url).query)['tk'][0]
                time.sleep(5)
                head_option['access-control-request-method'] = 'GET'
                head_option['access-control-request-headers'] = 'version'
                session.options('{}{}{}{}'.format('https://api-gateway.platoboost.com/v1/sessions/auth/', api, '/', hwid), headers=head_option, timeout=5)
                session.get('https://api-gateway.platoboost.com/v1/sessions/auth/{api}/{hwid}', headers=header, timeout=5)
                head_option['access-control-request-method'] = 'PUT'
                session.options('{}{}{}{}{}{}'.format('https://api-gateway.platoboost.com/v1/sessions/auth/', api, '/', hwid, '/', tk), headers=head_option, timeout=5)
                rokid_manager = session.put('{}{}{}{}{}{}'.format('https://api-gateway.platoboost.com/v1/sessions/auth/', api, '/', hwid, '/', tk), headers=header, timeout=5).json()
            else:
                return {'error': rokid_manager.get('message', 'Lỗi không xác định')}
        if 'gateway.platoboost.com' in rokid_manager.get('redirect', False):
            head_option['access-control-request-method'] = 'GET'
            session.options('{}{}{}{}'.format('https://api-gateway.platoboost.com/v1/authenticators/', api, '/', hwid), headers=head_option, timeout=5)
            rokid_manager = session.get('{}{}{}{}'.format('https://api-gateway.platoboost.com/v1/authenticators/', api, '/', hwid), headers=header, timeout=5).json()
            t = rokid_manager.get('minutesLeft', 0)
            return {'key': rokid_manager.get('key'), 'timeleft': t * 60 + 60}
        else:
            return {'error': 'Cant bypass Delta!'}
    except Exception as e:
        return {'error': 'Something went wrong!'}

def decrement_time(time_str):
    hours, minutes = map(int, time_str.replace('H', '').replace('M', '').split())
    if minutes > 0:
        minutes -= 1
    elif hours > 0:
        hours -= 1
        minutes = 59
    else:
        return '0H 0M'
    return '{}{}{}{}'.format(hours, 'H ', minutes, 'M')

def bypass_user_ids(accounts, executor_choice, minutes_left_dict=None):
    bypassed_results = []
    for package_name, _ in accounts:
        username = package_name
        try:
            if executor_choice == '1':
                hwid = get_hwid_platoboost()
                if hwid:
                    bypass_link = create_bypass_link(package_name, hwid)
                    try:
                        response = requests.get(bypass_link)
                        if response.status_code == 200:
                            result = response.json()
                            minutes_left = result.get('minutesLeft', '0H 0M')
                            if minutes_left_dict is not None:
                                minutes_left_dict[package_name] = minutes_left
                            bypassed_results.append((package_name, result))
                            print(Fore.GREEN + '{}{}{}'.format(username, ': Bypass successful with HWID - ', result) + Style.RESET_ALL)
                        else:
                            print(Fore.RED + '{}{}{}{}'.format(username, ': Bypass failed with status code ', response.status_code, ' using HWID') + Style.RESET_ALL)
                    except Exception as e:
                        print(Fore.RED + '{}{}{}'.format(username, ': Error using HWID - ', str(e)) + Style.RESET_ALL)
            elif executor_choice == '2':
                hwid = get_hwid(package_name)
                if hwid:
                    bypass_link = create_fluxus_bypass_link(hwid)
                    try:
                        response = requests.get(bypass_link)
                        if response.status_code == 200:
                            bypassed_results.append((package_name, response.json()))
                            print(Fore.GREEN + '{}{}{}'.format(username, ': Fluxus Bypass successful - ', response.json()) + Style.RESET_ALL)
                        else:
                            print(Fore.RED + '{}{}{}'.format(username, ': Fluxus Bypass failed with status code ', response.status_code) + Style.RESET_ALL)
                    except Exception as e:
                        print(Fore.RED + '{}{}{}'.format(username, ': Error during Fluxus Bypass - ', str(e)) + Style.RESET_ALL)
                else:
                    print(Fore.RED + '{}{}'.format(username, ': Failed to retrieve HWID for Fluxus') + Style.RESET_ALL)
        except Exception as bypass_error:
            print(Fore.RED + '{}{}{}{}'.format('Error during bypass for ', package_name, ': ', bypass_error) + Style.RESET_ALL)
            continue
    return bypassed_results
detect_and_write_lua_script()

def read_roblox_data(data_path, retries=3):
    attempt = 0
    while attempt < retries:
        try:
            with open(data_path, 'r') as file:
                data = json.load(file)
                user_id = data.get('UserId')
                username = data.get('Username')
                if user_id is not None and username is not None:
                    return (user_id, username)
                else:
                    attempt += 1
        except Exception as e:
            attempt += 1
            time.sleep(1)
    return (False, False)

def find_roblox_data_paths():
    base_path = '/data/data'
    paths = []
    for folder in os.listdir(base_path):
        if folder.startswith('com.roblox.') and folder != 'com.roblox.client':
            path = os.path.join(base_path, folder, 'files/appData/LocalStorage/appStorage.json')
            if os.path.isfile(path):
                paths.append(path)
    return paths

def logout_account(userid, username, data_path):
    try:
        roblox_package = data_path.split(os.sep)[3]
        force_roblox(roblox_package)
        appstorage_path = os.path.join(data_path)
        print('---------------------------------------------------------------------------')
        print('{}{}{}{}'.format('Logging out account: ', username, ', path: ', appstorage_path))
        os.remove(appstorage_path)
        logged_in_usernames.remove(username)
        print('{}{}'.format('Logged out account: ', username))
        print('---------------------------------------------------------------------------')
    except Exception as e:
        print('{}{}'.format('Logged out account: ', username))

def force_roblox(packages):
    try:
        full_command = '{}{}'.format('pkill -f ', packages)
        subprocess.run(full_command, check=True, timeout=10, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.TimeoutExpired:
        pass
    except subprocess.CalledProcessError as e:
        pass
    time.sleep(1)

def logout_roblox():
    global logged_in_usernames
    roblox_paths = find_roblox_data_paths()
    if not roblox_paths:
        print('No Roblox accounts found.')
        return
    accounts = []
    print((lambda: (lambda: (lambda: h2o(list(map(o2, ['[', ' ', 'R', 'o', 'k', 'i', 'd', ' ', 'M', 'a', 'n', 'a', 'g', 'e', 'r', ' ', ']', ' ', '-', '>', ' ', 'A', 'v', 'a', 'i', 'l', 'a', 'b', 'l', 'e', ' ', 'R', 'o', 'b', 'l', 'o', 'x', ' ', 'a', 'c', 'c', 'o', 'u', 'n', 't', 's', ':']))))())())())
    for i, data_path in enumerate(roblox_paths, start=1):
        userid, username = read_roblox_data(data_path)
        if userid and username:
            accounts.append((userid, username, data_path))
            print('{}{}{}{}{}'.format(i, '. Username: ', username, ', UserId: ', userid))
    if not accounts:
        print('No Roblox accounts found.')
        return
    print('Enter the number of the account to log out, 0 to log out all accounts, or q to quit:')
    choice = safe_input().strip()
    if choice.lower() == 'q':
        return
    try:
        if choice == '0':
            for userid, username, data_path in accounts:
                logout_account(userid, username, data_path)
        else:
            choice_index = int(choice) - 1
            if 0 <= choice_index < len(accounts):
                userid, username, data_path = accounts[choice_index]
                logout_account(userid, username, data_path)
            else:
                print('Invalid choice. Choice index out of range.')
    except ValueError:
        print('Invalid input. Please enter a number.')
    except Exception as e:
        import traceback
        traceback.print_exc()
        print('{}{}'.format('Error: ', e))
logged_in_usernames = set()

def check_cookie_validity(cookie):
    url = 'https://users.roblox.com/v1/users/authenticated'
    headers = {'Cookie': '{}{}'.format('.ROBLOSECURITY=', cookie), 'User-Agent': 'Mozilla/5.0', 'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print('{}{}'.format(Fore.GREEN, 'Cookie is alive!'))
        user_data = response.json()
        print('{}{}{}{}{}'.format('Logged in as: ', user_data['name'], ' (User ID: ', user_data['id'], ')'))
        return True
    elif response.status_code == 401:
        print('{}{}'.format(Fore.RED, 'Cookie is dead or invalid!'))
        return False
    else:
        print('{}{}{}'.format(Fore.YELLOW, 'Unexpected response. Status Code: ', response.status_code))
        print('{}{}'.format('Response: ', response.text))
        return False

def check_cookies_from_file(file_path):
    folder_name = 'Cookies Storage'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    live_file_path = os.path.join(folder_name, 'live.txt')
    dead_file_path = os.path.join(folder_name, 'dead.txt')
    if not os.path.exists(file_path):
        print('{}{}{}{}'.format(Fore.RED, 'File ', file_path, " doesn't exist. Creating one..."))
        with open(file_path, 'w') as file:
            file.write('')
        print('{}{}{}{}'.format(Fore.GREEN, 'Created ', file_path, ". Add cookies in it with 'username:password:cookie' or 'cookie' format and try again!"))
        return
    with open(file_path, 'r') as file:
        credentials = file.readlines()
    open(live_file_path, 'w').close()
    open(dead_file_path, 'w').close()
    total_cookies = len(credentials)
    live_cookies = 0
    dead_cookies = 0
    for idx, raw_cred in enumerate(credentials, 1):
        raw_cred = raw_cred.strip()
        username, password, cookie = (None, None, None)
        if raw_cred.count(':') >= 2:
            parts = raw_cred.split(':')
            username = parts[0]
            password = parts[1]
            cookie = ':'.join(parts[2:])
        else:
            cookie = raw_cred
        print('{}{}{}{}'.format(Fore.LIGHTBLACK_EX, 'Checking cookie ', idx, '...'))
        if check_cookie_validity(cookie):
            live_cookies += 1
            with open(live_file_path, 'a') as live_file:
                if username and password:
                    live_file.write('{}{}{}{}{}{}'.format(username, ':', password, ':', cookie, '\n'))
                else:
                    live_file.write('{}{}'.format(cookie, '\n'))
        else:
            dead_cookies += 1
            with open(dead_file_path, 'a') as dead_file:
                if username and password:
                    dead_file.write('{}{}{}{}{}{}'.format(username, ':', password, ':', cookie, '\n'))
                else:
                    dead_file.write('{}{}'.format(cookie, '\n'))
    print('----------------------------------------------------------------------')
    print('{}{}{}{}'.format('\n', Fore.CYAN, 'Total Cookies: ', total_cookies))
    print('{}{}{}'.format(Fore.GREEN, 'Live Cookies: ', live_cookies))
    print('{}{}{}'.format(Fore.RED, 'Dead Cookies: ', dead_cookies))

def create_autoexc_folder():
    downloads_path = '/sdcard/download'
    autoexc_folder = os.path.join(downloads_path, 'Autoexc')
    if not os.path.exists(autoexc_folder):
        print('{}{}'.format('Creating folder: ', autoexc_folder))
        os.makedirs(autoexc_folder)
    else:
        print('{}{}'.format("'Autoexc' folder already exists: ", autoexc_folder))
    return autoexc_folder

def push_autoexc_files():
    autoexc_folder = create_autoexc_folder()
    executors = {'Fluxus': '/storage/emulated/0/Fluxus/Autoexec', 'Codex': '/storage/emulated/0/Codex/Autoexec', 'Arceus X': '/storage/emulated/0/Arceus X/Autoexec', 'Delta': '/storage/emulated/0/Delta/Autoexec', 'Cryptic': '/storage/emulated/0/Cryptic/Autoexec'}
    txt_files = [f for f in os.listdir(autoexc_folder) if f.endswith('.txt')]
    if not txt_files:
        print('{}{}{}'.format('No .txt files found in ', autoexc_folder, '.'))
        return
    for executor_name, executor_path in executors.items():
        if os.path.exists(executor_path):
            for txt_file in txt_files:
                file_path = os.path.join(autoexc_folder, txt_file)
                destination = os.path.join(executor_path, txt_file)
                try:
                    shutil.copy(file_path, destination)
                    print(Fore.GREEN + '{}{}{}{}'.format('[ Rokid Manager ] -> Pushed your scripts to ', executor_name, ': ', destination))
                except Exception as e:
                    print(Fore.RED + '{}{}{}{}'.format('[ Rokid Manager ] -> Failed to push your scripts to ', executor_name, ': ', e))
SUCCESS_COLOR = '[92m'
FAILURE_COLOR = '[91m'
RESET_COLOR = '[0m'
SEPARATOR = '---------------------------------------------------------------------------------------'
successful_blocks = 0
failed_blocks = 0
lock = threading.Lock()

def extract_error_message(response):
    try:
        return response.json()['errors'][0]['message']
    except:
        return 'Not Found'

def get_userid_from_cookie(session, cookie, userids):
    try:
        response = session.get('https://users.roblox.com/v1/users/authenticated', cookies={'.ROBLOSECURITY': cookie}, timeout=3)
        user_data = response.json()
        with lock:
            userids.append(user_data.get('id'))
    except requests.exceptions.RequestException as e:
        print('{}{}{}{}'.format(FAILURE_COLOR, 'Failed to retrieve user ID: ', e, RESET_COLOR))

def block_users(session, cookie, userids):
    global successful_blocks, failed_blocks
    try:
        response = session.post('https://auth.roblox.com/v2/login', cookies={'.ROBLOSECURITY': cookie}, timeout=3)
        csrf_token = response.headers.get('X-CSRF-TOKEN', '')
        names = session.get('https://users.roblox.com/v1/users/authenticated', cookies={'.ROBLOSECURITY': str(cookie).strip()}, timeout=3)
        name = names.json().get('name', 'Not Found')
        for userid in userids:
            try:
                response = session.post('{}{}{}'.format('https://accountsettings.roblox.com/v1/users/', userid, '/block'), cookies={'.ROBLOSECURITY': cookie}, headers={'X-CSRF-TOKEN': csrf_token}, timeout=3)
                with lock:
                    if response.status_code == 200:
                        successful_blocks += 1
                        print(SEPARATOR)
                        print('{}{}{}{}{}{}'.format(SUCCESS_COLOR, "[ Rokid Manager ] -> ✓ SUCCESS: Account '", name, "' blocked user with ID ", userid, RESET_COLOR))
                        print(SEPARATOR)
                    else:
                        failed_blocks += 1
                        error_message = extract_error_message(response)
                        print(SEPARATOR)
                        print('{}{}{}{}{}'.format(FAILURE_COLOR, "[ Rokid Manager ] -> ✗ FAILURE: Account '", name, "' could not block user with ID ", userid))
                        print('{}{}{}'.format('    Reason: ', error_message, RESET_COLOR))
                        print(SEPARATOR)
            except requests.exceptions.RequestException as e:
                print('{}{}{}{}'.format(FAILURE_COLOR, 'Request error: ', e, RESET_COLOR))
    except requests.exceptions.RequestException as e:
        print('{}{}{}{}'.format(FAILURE_COLOR, 'Failed to authenticate: ', e, RESET_COLOR))

def block_worker(cookie, userids):
    with requests.Session() as session:
        block_users(session, cookie, userids)

def user_id_worker(cookie, userids):
    with requests.Session() as session:
        get_userid_from_cookie(session, cookie, userids)

def block_accounts():
    start_time = datetime.now()
    if not os.path.exists('cookie.txt'):
        print('{}{}{}'.format(FAILURE_COLOR, "[ Rokid Manager ] -> Error: 'cookie.txt' file not found!", RESET_COLOR))
        return
    with open('cookie.txt', 'r') as file:
        cookies = []
        for line in file:
            line = line.strip()
            if line.count(':') >= 2:
                cookies.append(':'.join(line.split(':')[2:]))
            else:
                cookies.append(line)

    def chunkify(lst, chunk_size):
                for i in range(0, len(lst), chunk_size):
                    yield lst[i:i + chunk_size]
    cookie_chunks = list(chunkify(cookies, 100))
    userids = []
    for chunk in cookie_chunks:
        userids = []
        threads = []
        for cookie in chunk:
            t = threading.Thread(target=user_id_worker, args=(cookie, userids))
            t.start()
            threads.append(t)
        for t in threads:
            t.join()
        threads = []
        for cookie in chunk:
            t = threading.Thread(target=block_worker, args=(cookie, userids))
            t.start()
            threads.append(t)
        for t in threads:
            t.join()
    end_time = datetime.now()
    elapsed_time = end_time - start_time
    print(SEPARATOR)
    print('{}{}{}{}'.format(SUCCESS_COLOR, '[ Rokid Manager ] -> Total successful blocks: ', successful_blocks, RESET_COLOR))
    print('{}{}{}{}'.format(FAILURE_COLOR, '[ Rokid Manager ] -> Total failed blocks: ', failed_blocks, RESET_COLOR))
    print('{}{}{}{}'.format('Time: ', elapsed_time.total_seconds(), ' seconds. Total cookies: ', len(cookies)))
    print(SEPARATOR)
    safe_input('Press Enter to exit ')
SUCCESS_COLOR = '[92m'
FAILURE_COLOR = '[91m'
RESET_COLOR = '[0m'
SEPARATOR = '---------------------------------------------------------------------------------------'
successful_unblocks = 0
failed_unblocks = 0
lock = threading.Lock()

def extract_error_message(response):
    'Extract error message from the response if available.'
    try:
        return response.json()['errors'][0]['message']
    except:
        return 'Not Found'

def get_userid_from_cookie(session, cookie, userids):
    'Get the user ID from a given cookie.'
    response = session.get('https://users.roblox.com/v1/users/authenticated', cookies={'.ROBLOSECURITY': cookie}, timeout=3)
    user_data = response.json()
    userids.append(user_data.get('id'))

def worker_get_userid(cookie, userids):
    'Worker function to get user ID from cookie.'
    with requests.Session() as session:
        get_userid_from_cookie(session, cookie, userids)

def unblock_users(session, cookie, userids):
    'Unblock users with the given cookie and user IDs.'
    global successful_unblocks, failed_unblocks
    response = session.post('https://auth.roblox.com/v2/login', cookies={'.ROBLOSECURITY': cookie}, timeout=3)
    csrf_token = response.headers['X-CSRF-TOKEN']
    names = session.get('https://users.roblox.com/v1/users/authenticated', cookies={'.ROBLOSECURITY': str(cookie).strip()}, timeout=3)
    try:
        name = names.json()['name']
    except:
        name = 'Not Found'
    for userid in userids:
        try:
            response = session.post('{}{}{}'.format('https://accountsettings.roblox.com/v1/users/', userid, '/unblock'), cookies={'.ROBLOSECURITY': cookie}, headers={'X-CSRF-TOKEN': csrf_token}, timeout=3)
        except:
            pass
        with lock:
            if response.status_code == 200:
                successful_unblocks += 1
                print(SEPARATOR)
                print('{}{}{}{}{}{}'.format(SUCCESS_COLOR, "[ Rokid Manager ] -> ✓ SUCCESS: Account '", name, "' unblocked user with ID ", userid, RESET_COLOR))
                print(SEPARATOR)
            else:
                failed_unblocks += 1
                error_message = response.json().get('errors', [{'message': 'Unknown error'}])[0]['message']
                print(SEPARATOR)
                print('{}{}{}{}{}'.format(FAILURE_COLOR, "[ Rokid Manager ] -> ✗ FAILURE: Account '", name, "' could not unblock user with ID ", userid))
                print('{}{}{}'.format('    Reason: ', error_message, RESET_COLOR))
                print(SEPARATOR)

def worker_unblock_users(cookie, userids):
    'Worker function to unblock users.'
    with requests.Session() as session:
        unblock_users(session, cookie, userids)

def unblock():
    'Main function to handle the unblocking process.'
    start_time = datetime.now()
    credentials = []
    with open('cookie.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line.count(':') >= 2:
                parts = line.split(':')
                username = parts[0]
                password = parts[1]
                cookie = ':'.join(parts[2:])
                credentials.append((username, password, cookie))
            else:
                credentials.append((None, None, line))

    def chunk_list(lst, chunk_size):
                for i in range(0, len(lst), chunk_size):
                    yield lst[i:i + chunk_size]
    credential_chunks = list(chunk_list(credentials, 100))
    for chunk in credential_chunks:
        userids = []
        threads = []
        for cred in chunk:
            t = threading.Thread(target=worker_get_userid, args=(cred[2], userids))
            t.start()
            threads.append(t)
        for t in threads:
            t.join()
        threads = []
        for cred in chunk:
            t = threading.Thread(target=worker_unblock_users, args=(cred[2], userids))
            t.start()
            threads.append(t)
        for t in threads:
            t.join()
    end_time = datetime.now()
    elapsed_time = end_time - start_time
    print(SEPARATOR)
    print('{}{}{}{}'.format(SUCCESS_COLOR, '[ Rokid Manager ] -> Total successful unblocks: ', successful_unblocks, RESET_COLOR))
    print('{}{}{}{}'.format(FAILURE_COLOR, '[ Rokid Manager ] -> Total failed unblocks: ', failed_unblocks, RESET_COLOR))
    print('{}{}{}{}'.format('Time: ', elapsed_time.total_seconds(), ' seconds. Total credentials processed: ', len(credentials)))
    print(SEPARATOR)
    safe_input('Press Enter to exit ')

def main_block_menu():
    clear_console()
    print_header()
    while True:
        print('----------------------------------------------------------------------')
        print(Fore.LIGHTBLUE_EX + 'Rokid Manager With Love :3')
        print('1. Block')
        print('2. UnBlock')
        print('3. Exit')
        choice = safe_input('Select an option : ')
        if choice == '1':
            block_accounts()
            clear_console()
            print_header()
        elif choice == '2':
            unblock()
            safe_input()
            clear_console()
            print_header()
        elif choice == '3':
            break
            main()
        else:
            print('{}{}'.format(Fore.RED, 'Invalid option | Please try again !'))
            safe_input(Fore.GREEN + 'Press Enter to exit...' + Style.RESET_ALL)
            clear_console()
            print_header()

def delete_roblox_cache():
    base_path = '/data/data'
    for folder in os.listdir(base_path):
        if folder.startswith('com.roblox.'):
            cache_path = os.path.join(base_path, folder, 'cache')
            if os.path.exists(cache_path):
                try:
                    shutil.rmtree(cache_path)
                except Exception as e:
                    pass

def check_authencation_changepass():
    github_raw_link = 'https://raw.githubusercontent.com/thieusitinks/Rokid-Manager/refs/heads/main/ChangePassAuthencator'
    try:
        response = requests.get(github_raw_link)
        response.raise_for_status()
        content = response.text.strip().lower()
        if content == 'true':
            print(Fore.GREEN + 'Authorized' + Style.RESET_ALL)
            return True
        else:
            print(Fore.RED + 'Not Authorized' + Style.RESET_ALL)
            time.sleep(3)
            clear_console()
            sys.exit(1)
    except requests.RequestException as e:
        print('{}{}'.format('An error occurred: ', e))
        sys.exit(1)
logger.remove()
logger.add(sink=sys.stdout, format='{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}', level='INFO')
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

CONFIG_FILE = os.path.join(SCRIPT_DIR, 'config-cp.json')
BASE_DIR = os.path.join(SCRIPT_DIR, 'Password Storage')
ACC_FILE = os.path.join(BASE_DIR, 'acc.txt')
DONE_FILE = os.path.join(BASE_DIR, 'done.txt')

def load_config():
    default_config = {'threads': 5, 'wait_time': 60, 'custom_password': 'RokidManagerOnTop', 'generate_random_password': False, 'random_password_length': 12}
    if not os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'w') as f:
            json.dump(default_config, f, indent=4)
        logger.info('{}{}'.format(Fore.GREEN, 'Created default config.json'))
    with open(CONFIG_FILE, 'r') as f:
        return json.load(f)
config = load_config()
THREADS = config.get('threads', 5)
WAIT_TIME = config.get('wait_time', 61)
CUSTOM_PASSWORD = config.get('custom_password', 'hello1212')
GENERATE_RANDOM_PASSWORD = config.get('generate_random_password', False)
RANDOM_PASSWORD_LENGTH = config.get('random_password_length', 12)
os.makedirs(BASE_DIR, exist_ok=True)
if not os.path.exists(ACC_FILE):
    with open(ACC_FILE, 'w') as f:
        f.write('')
    logger.info('{}{}'.format(Fore.GREEN, 'Created acc.txt, write user:pass:cookie to start process.'))
if not os.path.exists(DONE_FILE):
    with open(DONE_FILE, 'w') as f:
        f.write('')
    logger.info('{}{}'.format(Fore.GREEN, 'Created done.txt'))

class Account:

    def __init__(self, username, password, cookie):
        self.Username = username
        self.Password = password
        self.NewPassword = self.generate_new_password()
        self.Cookie = cookie
        self.KyTuCuoiCookie = ''

    def generate_new_password(self):
        if GENERATE_RANDOM_PASSWORD:
            return ''.join(random.choices(string.ascii_letters + string.digits, k=RANDOM_PASSWORD_LENGTH))
        return CUSTOM_PASSWORD

def try_change_password(account, url):

    def get_csrf_token(cookie):
                try:
                    csrf_request = requests.post('https://roblox.com/', cookies={'.ROBLOSECURITY': cookie}, headers={'Referer': 'https://www.roblox.com/'})
                    if csrf_request.status_code == 403:
                        return csrf_request.headers.get('x-csrf-token')
                except requests.RequestException as e:
                    logger.error('{}{}{}'.format(Fore.RED, 'Error while fetching CSRF token: ', e))
                return None

    def make_request(request_url, csrf_token):
                try:
                    return requests.post(request_url, cookies={'.ROBLOSECURITY': account.Cookie}, headers={'Referer': 'https://www.roblox.com/', 'X-CSRF-TOKEN': csrf_token, 'Content-Type': 'application/x-www-form-urlencoded'}, data={'currentPassword': account.Password, 'newPassword': account.NewPassword})
                except requests.RequestException as e:
                    logger.error('{}{}{}'.format(Fore.RED, 'Error while changing password: ', e))
                    return None
    token = get_csrf_token(account.Cookie)
    if not token:
        logger.warning('{}{}{}'.format(Fore.YELLOW, 'Failed to get CSRF token for ', account.Username))
        return False
    request = make_request(url, token)
    if request and request.ok and (request.status_code == 200):
        new_cookie = request.cookies.get('.ROBLOSECURITY')
        if new_cookie:
            account.Cookie = new_cookie
            account.KyTuCuoiCookie = new_cookie[-10:]
            return True
    return False

def change_password(account):
    urls = ['https://auth.roblox.com/v1/user/passwords/change', 'https://auth.roblox.com/v2/user/passwords/change']
    for url in urls:
        if try_change_password(account, url):
            return True
    return False

def process_account(account_info):
    username, password, cookie = account_info
    account = Account(username, password, cookie)
    if change_password(account):
        logger.info('{}{}{}'.format(Fore.GREEN, '[SUCCESS] Password successfully changed for ', account.Username))
        return ('{}{}{}{}{}{}'.format(account.Username, ':', account.NewPassword, ':', account.Cookie, '\n'), account_info)
    else:
        logger.error('{}{}{}'.format(Fore.RED, '[FAIL] Failed to change password for ', account.Username))
        return (None, None)

def process_accounts():
    check_authencation_changepass()
    while True:
        try:
            with open(ACC_FILE, 'r') as acc_file:
                accounts = [line.strip().split(':', 2) for line in acc_file.readlines() if len(line.strip().split(':', 2)) == 3]
        except FileNotFoundError:
            logger.error('{}{}'.format(Fore.RED, 'acc.txt not found. Please create the file with valid account data.'))
            break
        if not accounts:
            logger.info('{}'.format('No accounts left to process.'))
            break
        accounts_to_process = accounts[:THREADS]
        with open(DONE_FILE, 'a') as done_file:
            with ThreadPoolExecutor(max_workers=THREADS) as executor:
                results = executor.map(process_account, accounts_to_process)
            updated_accounts = accounts.copy()
            for result, account_info in results:
                if result:
                    done_file.write(result)
                    updated_accounts.remove(account_info)
            with open(ACC_FILE, 'w') as acc_file:
                for acc in updated_accounts:
                    acc_file.write(':'.join(acc) + (lambda: (lambda: (lambda: h2o(list(map(o2, ['\n']))))())())())
        logger.info('{}{}{}{}'.format(Fore.CYAN, '[ Rokid Manager ] -> Waiting ', WAIT_TIME, ' seconds before processing the next batch...'))
        time.sleep(WAIT_TIME)

def find_folder_starting_with(base_path, prefix):
    try:
        for folder in os.listdir(base_path):
            if folder.startswith(prefix):
                return os.path.join(base_path, folder)
        return None
    except FileNotFoundError:
        print(Fore.RED + '{}{}'.format('Base path not found: ', base_path) + Style.RESET_ALL)
        return None

def extract_user_info(json_path):
    try:
        if not os.path.exists(json_path):
            return None
        with open(json_path, 'r') as file:
            data = json.load(file)
            username = data.get('Username')
            user_id = data.get('UserId')
            if username and user_id:
                return (username, user_id)
            else:
                return None
    except json.JSONDecodeError:
        return None
    except Exception as e:
        return None

def find_other_roblox_data_paths():
    base_path = '/data/data'
    paths = []
    try:
        for folder in os.listdir(base_path):
            if folder.lower().startswith('com.roblox.'):
                potential_path = os.path.join(base_path, folder)
                paths.append(potential_path)
    except FileNotFoundError:
        pass
    return paths

def get_cookies_from_path(cookies_db_path):
    cookies = []
    if not os.path.exists(cookies_db_path):
        return cookies
    try:
        conn = sqlite3.connect(cookies_db_path)
        cursor = conn.cursor()
        query = 'SELECT value FROM cookies WHERE host_key LIKE %roblox.com%'
        cursor.execute(query)
        rows = cursor.fetchall()
        cookie_pattern = '_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_.*?)$'
        for row in rows:
            cookie_candidate = row[0]
            cookie_match = re.search(cookie_pattern, cookie_candidate)
            if cookie_match:
                cookies.append(cookie_match.group(1))
        cursor.close()
        conn.close()
    except sqlite3.Error:
        pass
    except Exception:
        pass
    return cookies

def display_statistics(roblox_paths):
    print(Fore.CYAN + 'Roblox Client Paths Detected:' + Style.RESET_ALL)
    statistics = []
    for index, path in enumerate(roblox_paths):
        json_path = os.path.join(path, 'files/appData/LocalStorage/appStorage.json')
        user_info = extract_user_info(json_path)
        username = user_info[0] if user_info else 'Unknown'
        user_id = user_info[1] if user_info else 'Unknown'
        print('{}{}{}{}{}{}{}'.format(index + 1, '. Username: ', username, ' | User ID: ', user_id, ' | Path: ', path))
        statistics.append((username, user_id, path))
    return statistics

def auto_get_cookies_from_paths(selected_paths):
    found_cookies = []
    for path in selected_paths:
        cookies_db_path = os.path.join(path, 'app_webview', 'Default', 'Cookies')
        cookies = get_cookies_from_path(cookies_db_path)
        found_cookies.extend(cookies)
    if found_cookies:
        storage_folder = 'Cookies Storage'
        os.makedirs(storage_folder, exist_ok=True)
        output_file = os.path.join(storage_folder, 'cookies-data.txt')
        with open(output_file, 'w') as output:
            output.write((lambda: (lambda: (lambda: h2o(list(map(o2, ['\n']))))())())().join(found_cookies))
        print(Fore.GREEN + '{}{}'.format('[ Rokid Manager ] -> Cookies saved to ', output_file) + Style.RESET_ALL)
    else:
        print(Fore.RED + (lambda: (lambda: (lambda: h2o(list(map(o2, ['[', ' ', 'R', 'o', 'k', 'i', 'd', ' ', 'M', 'a', 'n', 'a', 'g', 'e', 'r', ' ', ']', ' ', '-', '>', ' ', 'N', 'o', ' ', 'v', 'a', 'l', 'i', 'd', ' ', 'c', 'o', 'o', 'k', 'i', 'e', 's', ' ', 'f', 'o', 'u', 'n', 'd', ' ', 'i', 'n', ' ', 't', 'h', 'e', ' ', 's', 'e', 'l', 'e', 'c', 't', 'e', 'd', ' ', 'p', 'a', 't', 'h', 's', '.']))))())())() + Style.RESET_ALL)

def getcookie_process():
    roblox_paths = find_other_roblox_data_paths()
    if not roblox_paths:
        print(Fore.RED + 'No Roblox paths detected.' + Style.RESET_ALL)
        return
    statistics = display_statistics(roblox_paths)
    while True:
        print(Fore.YELLOW + (lambda: (lambda: (lambda: h2o(list(map(o2, ['\n', '[', ' ', 'R', 'o', 'k', 'i', 'd', ' ', 'M', 'a', 'n', 'a', 'g', 'e', 'r', ' ', ']', ' ', '-', '>', ' ', 'C', 'h', 'o', 'o', 's', 'e', ' ', 'a', 'n', ' ', 'o', 'p', 't', 'i', 'o', 'n', ':']))))())())() + Style.RESET_ALL)
        print('q - Quit to Main Menu')
        print('0 - Get cookies from all paths')
        for index, (username, user_id, path) in enumerate(statistics):
            print('{}{}{}'.format(index + 1, ' - Get cookies from path: ', path))
        choice = safe_input('Enter your choice: ').strip()
        if choice.lower() == 'q':
            return
        if choice.isdigit():
            choice = int(choice)
            if choice == 0:
                auto_get_cookies_from_paths([stat[2] for stat in statistics])
                break
            elif 1 <= choice <= len(statistics):
                selected_path = [statistics[choice - 1][2]]
                auto_get_cookies_from_paths(selected_path)
                break
            else:
                print(Fore.RED + (lambda: (lambda: (lambda: h2o(list(map(o2, ['[', ' ', 'R', 'o', 'k', 'i', 'd', ' ', 'M', 'a', 'n', 'a', 'g', 'e', 'r', ' ', ']', ' ', '-', '>', ' ', 'I', 'n', 'v', 'a', 'l', 'i', 'd', ' ', 'c', 'h', 'o', 'i', 'c', 'e', '.', ' ', 'P', 'l', 'e', 'a', 's', 'e', ' ', 't', 'r', 'y', ' ', 'a', 'g', 'a', 'i', 'n', '.']))))())())() + Style.RESET_ALL)
        else:
            print(Fore.RED + (lambda: (lambda: (lambda: h2o(list(map(o2, ['[', ' ', 'R', 'o', 'k', 'i', 'd', ' ', 'M', 'a', 'n', 'a', 'g', 'e', 'r', ' ', ']', ' ', '-', '>', ' ', 'I', 'n', 'v', 'a', 'l', 'i', 'd', ' ', 'c', 'h', 'o', 'i', 'c', 'e', '.', ' ', 'C', 'h', 'o', 'o', 's', 'e', ' ', 'q', ' ', 't', 'o', ' ', 'q', 'u', 'i', 't', ' ', '|', ' ', '0', ' ', 't', 'o', ' ', 'g', 'e', 't', ' ', 'a', 'l', 'l', ' ', 'c', 'o', 'o', 'k', 'i', 'e', 's']))))())())() + Style.RESET_ALL)
            print_header()
            clear_console()

def main():
    clear_screen()
    load_cache()
    print_header()
    _first_draw = True
    while True:
        if _first_draw:
            clear_screen()
            print_header()
            menu_options = ['Start Auto Rejoin', 'Set User IDs for Each Package', 'Same Game ID or Private Server Link',
                            'Different Private Server or Game ID', 'Clear User IDs and/or Server Links', 'List',
                            'Auto Setup User IDs', 'Bypass Start Patched)', 'Same HWID Fluxus', 'Auto Login via Cookie',
                            'Auto Logout', 'Check Cookies', 'Setup webhook', 'Set Up AutoExec',
                            'Block / UnBlock Account', 'Auto Change Password', 'Get Cookie From Logged Account', 'Exit']
            create_dynamic_menu(menu_options)
            _first_draw = False
        setup_type = safe_input(Fore.LIGHTMAGENTA_EX + 'Enter choice: ' + Style.RESET_ALL)
        if not setup_type.strip():
            continue
        _first_draw = True

        # ─────────────────────────────────────────────────────────────
        # Вспомогательная функция: проверить executor,
        # при False → ждать 60с → проверить снова → при False → continue
        # Возвращает True если executor загружен, False если нет (timeout)
        # ─────────────────────────────────────────────────────────────
        def executor_check_with_wait(username, package_name, package_statuses):
            if check_executor_status(username, continuous=False):
                package_statuses[package_name]['Status'] = (
                    Fore.GREEN + 'Executor loaded successfully for {}'.format(username) + Style.RESET_ALL
                )
                update_status_table(package_statuses)
                return True
            else:
                print('Executor did not load for {} (username: {}). Waiting 60 seconds...'.format(
                    package_name, username))
                package_statuses[package_name]['Status'] = (
                    Fore.YELLOW + 'Executor not loaded, waiting 60s...' + Style.RESET_ALL
                )
                update_status_table(package_statuses)
                time.sleep(60)

                if check_executor_status(username, continuous=False):
                    package_statuses[package_name]['Status'] = (
                        Fore.GREEN + 'Executor loaded successfully for {} (after 60s)'.format(username) + Style.RESET_ALL
                    )
                    update_status_table(package_statuses)
                    return True
                else:
                    print('Executor still not loaded for {} after 60s, continuing...'.format(package_name))
                    package_statuses[package_name]['Status'] = (
                        Fore.YELLOW + 'Executor timeout after 60s, continuing...' + Style.RESET_ALL
                    )
                    update_status_table(package_statuses)
                    return False  # продолжаем код

        if setup_type == '1':
            server_links = load_server_links()
            accounts = load_accounts()
            if not accounts:
                print(Fore.RED + 'No user IDs set up yet! Please set them up before proceeding.' + Style.RESET_ALL)
                continue
            elif not server_links:
                print(Fore.RED + 'No game ID or private server link set up yet! Please set them up before proceeding.' + Style.RESET_ALL)
                continue
            try:
                print((lambda: (lambda: (lambda: h2o(list(map(o2, ['[', ' ', 'R', 'o', 'k', 'i', 'd', ' ', 'M', 'a', 'n',
                    'a', 'g', 'e', 'r', ' ', ']', ' ', '-', '>', ' ', 'I', 'f', ' ', 'Y', 'o', 'u', ' ', 'G', 'o', 't',
                    ' ', 'P', 'r', 'o', 'b', 'l', 'e', 'm', ' ', 'O', 'n', ' ', 'R', 'e', 'j', 'o', 'i', 'n', 'i', 'n',
                    'g', ' ', ',', ' ', 'P', 'l', 'z', ' ', 'U', 's', 'e', ' ', 'F', 'u', 'n', 'c', 't', 'i', 'o', 'n',
                    ' ', '7', ' ', 'F', 'o', 'r', ' ', 'S', 'e', 't', 'U', 'p', ' ', 'U', 's', 'e', 'r', 'n', 'a', 'm',
                    'e', ' ', 'C', 'o', 'r', 'r', 'e', 'c', 't', 'l', 'y', ' ', '!']))))())())())
                force_rejoin_interval = int(safe_input('Enter the force rejoin/kill Roblox interval in minutes: ')) * 60
                if force_rejoin_interval <= 0:
                    raise ValueError('The interval must be a positive integer.')
            except ValueError as ve:
                print(Fore.RED + 'Invalid input: {}. Please enter a valid interval in minutes.'.format(ve) + Style.RESET_ALL)
                safe_input(Fore.GREEN + 'Press Enter to return to the menu...' + Style.RESET_ALL)
                continue

            package_statuses = {}
            for package_name, server_link in server_links:
                package_statuses[package_name] = {
                    'Status': Fore.LIGHTCYAN_EX + 'Initializing' + Style.RESET_ALL,
                    'Username': get_username(accounts[server_links.index((package_name, server_link))][1])
                }
            update_status_table(package_statuses)
            kill_roblox_processes()
            time.sleep(2)
            num_packages = len(server_links)

            for package_name, server_link in server_links:
                try:
                    package_statuses[package_name]['Status'] = Fore.LIGHTCYAN_EX + 'Launching' + Style.RESET_ALL
                    update_status_table(package_statuses)
                    launch_roblox(package_name, server_link, num_packages, package_statuses)
                    package_statuses[package_name]['Status'] = Fore.GREEN + 'Joined' + Style.RESET_ALL
                    username = get_username(accounts[server_links.index((package_name, server_link))][1])
                    reset_executor_file(username)

                    # ── НОВАЯ ЛОГИКА: False → ждём 60с → ещё раз → если False → continue ──
                    executor_check_with_wait(username, package_name, package_statuses)
                    # независимо от результата — продолжаем следующий пакет

                except Exception as e:
                    print(Fore.RED + 'Error launching Roblox for {}: {}'.format(package_name, e) + Style.RESET_ALL)
                    package_statuses[package_name]['Status'] = Fore.RED + 'Launch failed' + Style.RESET_ALL
                update_status_table(package_statuses)

            start_time = time.time()
            while True:
                current_time = time.time()
                try:
                    for package_name, user_id in accounts:
                        try:
                            server_link = get_server_link(package_name, server_links)
                            if not server_link:
                                package_statuses[package_name]['Status'] = Fore.RED + 'Server link not found' + Style.RESET_ALL
                                update_status_table(package_statuses)
                                continue
                            username = get_username_from_id(user_id)
                            presence_type, last_location_current = check_user_online(user_id)
                            package_statuses[package_name]['Username'] = username
                            if presence_type == 2:
                                package_statuses[package_name]['Status'] = Fore.GREEN + 'In-Game' + Style.RESET_ALL
                                if not check_executor_status(username, continuous=False):
                                    print('Executor did not update for {} (username: {}). Waiting 60s...'.format(
                                        package_name, username))
                                    package_statuses[package_name]['Status'] = (
                                        Fore.YELLOW + 'Executor not updated, waiting 60s...' + Style.RESET_ALL
                                    )
                                    update_status_table(package_statuses)
                                    time.sleep(60)
                                    if not check_executor_status(username, continuous=False):
                                        print('Executor still not updated for {} after 60s, continuing...'.format(package_name))
                                        package_statuses[package_name]['Status'] = (
                                            Fore.YELLOW + 'Executor timeout, continuing...' + Style.RESET_ALL
                                        )
                                        update_status_table(package_statuses)
                                        # продолжаем — НЕ режоиним
                                    else:
                                        package_statuses[package_name]['Status'] = (
                                            Fore.GREEN + 'Executor OK after wait' + Style.RESET_ALL
                                        )
                                        update_status_table(package_statuses)
                            elif not is_roblox_running(package_name):
                                package_statuses[package_name]['Status'] = Fore.RED + 'Process Crashed, Relaunching' + Style.RESET_ALL
                                kill_roblox_process(package_name)
                                time.sleep(2)
                                launch_roblox(package_name, server_link, num_packages, package_statuses)
                                executor_check_with_wait(username, package_name, package_statuses)
                            elif last_location_current == 'Website':
                                package_statuses[package_name]['Status'] = Fore.RED + 'On Website, Rejoining' + Style.RESET_ALL
                                kill_roblox_process(package_name)
                                time.sleep(2)
                                launch_roblox(package_name, server_link, num_packages, package_statuses)
                                executor_check_with_wait(username, package_name, package_statuses)
                            else:
                                package_statuses[package_name]['Status'] = Fore.YELLOW + 'Not In-Game, Recently Active' + Style.RESET_ALL
                            update_status_table(package_statuses)
                            time.sleep(25)
                        except Exception as e:
                            print(Fore.RED + 'Error during rejoin process for {}: {}'.format(package_name, e) + Style.RESET_ALL)
                            package_statuses[package_name]['Status'] = Fore.RED + 'General error' + Style.RESET_ALL
                            update_status_table(package_statuses)

                    if current_time - start_time >= force_rejoin_interval:
                        print('Force killing Roblox processes due to time limit.')
                        kill_roblox_processes()
                        start_time = current_time
                        print(Fore.YELLOW + 'Waiting for 5 seconds before starting the rejoin process...' + Style.RESET_ALL)
                        time.sleep(5)
                        for package_name, server_link in server_links:
                            try:
                                package_statuses[package_name]['Status'] = Fore.RED + 'Rejoining' + Style.RESET_ALL
                                update_status_table(package_statuses)
                                launch_roblox(package_name, server_link, num_packages, package_statuses)
                                executor_check_with_wait(username, package_name, package_statuses)
                                package_statuses[package_name]['Status'] = Fore.GREEN + 'Joined' + Style.RESET_ALL
                            except Exception as e:
                                print(Fore.RED + 'Error rejoining Roblox for {}: {}'.format(package_name, e) + Style.RESET_ALL)
                        update_status_table(package_statuses)
                    time.sleep(90)
                except Exception as e:
                    print(Fore.RED + 'Critical error in auto rejoin loop: {}'.format(e) + Style.RESET_ALL)
                    time.sleep(60)
                    continue

        elif setup_type == '2':
            accounts = []
            packages = get_roblox_packages()
            for package_name in packages:
                user_input = safe_input('Enter the user ID or username for {}: '.format(package_name))
                user_id = None
                if user_input.isdigit():
                    user_id = user_input
                else:
                    print('Retrieving user ID for username: {}...'.format(user_input))
                    user_id = asyncio.run(get_user_id(user_input))
                    if user_id is None:
                        print(Fore.RED + 'Failed to retrieve user ID. Please enter the user ID manually.' + Style.RESET_ALL)
                        user_id = safe_input('Enter the user ID: ')
                accounts.append((package_name, user_id))
                print('Set {} to user ID: {}'.format(package_name, user_id))
            save_accounts(accounts)
            save_cache()
            print(Fore.GREEN + 'User IDs saved!' + Style.RESET_ALL)
            safe_input(Fore.GREEN + 'Press Enter to exit...' + Style.RESET_ALL)

        elif setup_type == '3':
            server_link = safe_input('Enter the game ID or private server link: ')
            formatted_link = format_server_link(server_link)
            if formatted_link:
                packages = get_roblox_packages()
                server_links = [(package_name, formatted_link) for package_name in packages]
                save_server_links(server_links)
                print(Fore.GREEN + 'Game ID or private server link saved successfully!' + Style.RESET_ALL)
            safe_input(Fore.GREEN + 'Press Enter to exit...' + Style.RESET_ALL)

        elif setup_type == '4':
            packages = get_roblox_packages()
            server_links = []
            for package_name in packages:
                server_link = safe_input('Enter the game ID or private server link for {}: '.format(package_name))
                formatted_link = format_server_link(server_link)
                if formatted_link:
                    server_links.append((package_name, formatted_link))
            save_server_links(server_links)
            safe_input(Fore.GREEN + 'Press Enter to exit...' + Style.RESET_ALL)

        elif setup_type == '5':
            clear_choice = safe_input(Fore.GREEN + 'What do you want to clear?\n1. Clear User IDs\n2. Clear Server Links\n3. Clear Both\nEnter choice: ' + Style.RESET_ALL)
            if clear_choice == '1':
                if os.path.exists(ACCOUNTS_FILE):
                    os.remove(ACCOUNTS_FILE)
                    print(Fore.GREEN + 'User IDs cleared successfully!' + Style.RESET_ALL)
                else:
                    print(Fore.YELLOW + "No such file: '{}' found to clear.".format(ACCOUNTS_FILE) + Style.RESET_ALL)
            elif clear_choice == '2':
                if os.path.exists(SERVER_LINKS_FILE):
                    os.remove(SERVER_LINKS_FILE)
                    print(Fore.GREEN + 'Server links cleared successfully!' + Style.RESET_ALL)
                else:
                    print(Fore.YELLOW + "No such file: '{}' found to clear.".format(SERVER_LINKS_FILE) + Style.RESET_ALL)
            elif clear_choice == '3':
                if os.path.exists(ACCOUNTS_FILE):
                    os.remove(ACCOUNTS_FILE)
                    print(Fore.GREEN + 'User IDs cleared successfully!' + Style.RESET_ALL)
                else:
                    print(Fore.YELLOW + "No such file: '{}' found to clear.".format(ACCOUNTS_FILE) + Style.RESET_ALL)
                if os.path.exists(SERVER_LINKS_FILE):
                    os.remove(SERVER_LINKS_FILE)
                    print(Fore.GREEN + 'Server links cleared successfully!' + Style.RESET_ALL)
                else:
                    print(Fore.YELLOW + "No such file: '{}' found to clear.".format(SERVER_LINKS_FILE) + Style.RESET_ALL)
            safe_input(Fore.GREEN + 'Press Enter to exit...' + Style.RESET_ALL)

        elif setup_type == '6':
            accounts = load_accounts()
            server_links = load_server_links()
            if accounts and server_links:
                headers = ['Account', 'Server', 'Game ID', 'Username']
                rows = [(package, server, game_id, get_username(game_id))
                        for (package, game_id), (_, server) in zip(accounts, server_links)]
                create_dynamic_table(headers, rows)
            else:
                print(Fore.RED + 'No accounts or server links to display.' + Style.RESET_ALL)
            safe_input(Fore.GREEN + 'Press Enter to return to the menu...' + Style.RESET_ALL)

        elif setup_type == '7':
            print(Fore.GREEN + 'Auto Setup User IDs from each packages appStorage.json...' + Style.RESET_ALL)
            packages = get_roblox_packages()
            accounts = []
            for package_name in packages:
                file_path = '/data/data/{}/files/appData/LocalStorage/appStorage.json'.format(package_name)
                user_id = find_userid_from_file(file_path)
                if user_id:
                    accounts.append((package_name, user_id))
                    print('Found UserId for {}: {}'.format(package_name, user_id))
                else:
                    print(Fore.RED + 'UserId not found for {}. Make sure the file path is correct.'.format(package_name) + Style.RESET_ALL)
            save_accounts(accounts)
            save_cache()
            print(Fore.GREEN + 'User IDs saved from appStorage.json!' + Style.RESET_ALL)
            server_link = safe_input('Enter the game ID or private server link: ')
            formatted_link = format_server_link(server_link)
            if formatted_link:
                server_links = [(package_name, formatted_link) for package_name in packages]
                save_server_links(server_links)
                print(Fore.GREEN + 'Game ID or private server link saved successfully!' + Style.RESET_ALL)
            safe_input(Fore.GREEN + 'Press Enter to exit...' + Style.RESET_ALL)

        elif setup_type == '8':
            accounts = load_accounts()
            server_links = load_server_links()
            last_bypass_time = time.time()
            if not accounts:
                print(Fore.RED + 'No user IDs set up yet! Please set them up before proceeding.' + Style.RESET_ALL)
                continue
            try:
                force_rejoin_interval = int(safe_input('Enter the force rejoin/kill Roblox interval in minutes: ')) * 60
                if force_rejoin_interval <= 0:
                    raise ValueError('The interval must be a positive integer.')
            except ValueError as ve:
                print(Fore.RED + 'Invalid input: {}. Please enter a valid interval in minutes.'.format(ve) + Style.RESET_ALL)
                safe_input(Fore.GREEN + 'Press Enter to return to the menu...' + Style.RESET_ALL)
                continue

            print(Fore.GREEN + 'Choose the executor:' + Style.RESET_ALL)
            print('1. Delta')
            print('2. Fluxus')
            executor_choice = safe_input('Enter your choice 1-2): ')
            if executor_choice not in ['1', '2']:
                print(Fore.RED + 'Invalid choice. Please enter a valid option.' + Style.RESET_ALL)
                continue

            minutes_left_dict = {} if executor_choice == '1' else None
            bypass_interval = None
            if executor_choice == '2':
                print(Fore.GREEN + 'Choose the bypass interval:' + Style.RESET_ALL)
                print('1. Every 30 minutes')
                print('2. Every 1 hour')
                print('3. Every 2 hours')
                print('4. Every 12 hours')
                interval_choice = safe_input('Enter your choice 1-4): ')
                bypass_interval_mapping = {'1': 30 * 60, '2': 60 * 60, '3': 2 * 60 * 60, '4': 12 * 60 * 60}
                bypass_interval = bypass_interval_mapping.get(interval_choice)
                if not bypass_interval:
                    print(Fore.RED + 'Invalid choice. Please enter a valid option.' + Style.RESET_ALL)
                    continue

            package_statuses = {}
            for package_name, _ in server_links:
                package_statuses[package_name] = {
                    'Status': Fore.LIGHTCYAN_EX + 'Initializing' + Style.RESET_ALL,
                    'Username': get_username(accounts[server_links.index((package_name, _))][1])
                }
            update_status_table(package_statuses)

            if executor_choice == '1':
                for package_name in accounts:
                    try:
                        if package_name not in minutes_left_dict or minutes_left_dict[package_name] == '0H 0M':
                            hwid = get_hwid_platoboost()
                            bypassed_links = bypass_user_ids([(package_name, None)], '1', minutes_left_dict)
                            if bypassed_links:
                                package_statuses[package_name]['Status'] = Fore.GREEN + 'Delta Bypass successful' + Style.RESET_ALL
                            else:
                                package_statuses[package_name]['Status'] = Fore.RED + 'Failed to bypass using Delta' + Style.RESET_ALL
                        else:
                            print(Fore.YELLOW + '{}: Waiting for {} before rebypass...'.format(
                                package_name, minutes_left_dict[package_name]) + Style.RESET_ALL)
                    except Exception as e:
                        package_statuses[package_name]['Status'] = Fore.RED + 'Error during Delta Bypass: {}'.format(e) + Style.RESET_ALL
                    update_status_table(package_statuses)
            elif executor_choice == '2':
                for package_name in accounts:
                    hwid = get_hwid(package_name)
                    if hwid:
                        bypass_link = create_fluxus_bypass_link(hwid)
                        try:
                            response = requests.get(bypass_link)
                            if response.status_code == 200:
                                bypass_result = response.json()
                                package_statuses[package_name]['Status'] = Fore.GREEN + 'Fluxus Bypass successful' + Style.RESET_ALL
                            else:
                                package_statuses[package_name]['Status'] = Fore.RED + 'Fluxus Bypass failed with status code {}'.format(
                                    response.status_code) + Style.RESET_ALL
                        except Exception as e:
                            package_statuses[package_name]['Status'] = Fore.RED + 'Error during Fluxus Bypass: {}'.format(e) + Style.RESET_ALL
                    else:
                        package_statuses[package_name]['Status'] = Fore.RED + 'Failed to retrieve HWID' + Style.RESET_ALL
                    update_status_table(package_statuses)

            print('Killing Roblox processes...')
            kill_roblox_processes()
            print(Fore.YELLOW + 'Waiting for 5 seconds before starting the rejoin process...' + Style.RESET_ALL)
            time.sleep(5)
            num_packages = len(server_links)

            for package_name, server_link in server_links:
                try:
                    launch_roblox(package_name, server_link, num_packages, package_statuses)
                    username = get_username(accounts[server_links.index((package_name, server_link))][1])
                    reset_executor_file(username)

                    # ── НОВАЯ ЛОГИКА ──
                    executor_check_with_wait(username, package_name, package_statuses)

                except Exception as e:
                    print(Fore.RED + 'Error launching Roblox for {}: {}'.format(package_name, e) + Style.RESET_ALL)
                    package_statuses[package_name]['Status'] = Fore.RED + 'Launch failed' + Style.RESET_ALL
                update_status_table(package_statuses)

            start_time = time.time()
            last_bypass_time = start_time
            try:
                while True:
                    current_time = time.time()
                    for package_name, user_id in accounts:
                        username = get_username(user_id) or user_id
                        presence_type, last_location_current = check_user_online(user_id)
                        package_statuses[package_name]['Username'] = username
                        if presence_type == 2:
                            package_statuses[package_name]['Status'] = Fore.GREEN + 'In-Game' + Style.RESET_ALL
                            if not check_executor_status(username, continuous=False):
                                print('Executor did not update for {} (username: {}). Waiting 60s...'.format(
                                    package_name, username))
                                package_statuses[package_name]['Status'] = (
                                    Fore.YELLOW + 'Executor not updated, waiting 60s...' + Style.RESET_ALL
                                )
                                update_status_table(package_statuses)
                                time.sleep(60)
                                if not check_executor_status(username, continuous=False):
                                    print('Executor still not updated for {} after 60s, continuing...'.format(package_name))
                                    package_statuses[package_name]['Status'] = (
                                        Fore.YELLOW + 'Executor timeout, continuing...' + Style.RESET_ALL
                                    )
                                    update_status_table(package_statuses)
                                else:
                                    package_statuses[package_name]['Status'] = (
                                        Fore.GREEN + 'Executor OK after wait' + Style.RESET_ALL
                                    )
                                    update_status_table(package_statuses)
                        elif not is_roblox_running(package_name):
                            package_statuses[package_name]['Status'] = Fore.RED + 'Process Crashed, Relaunching' + Style.RESET_ALL
                            kill_roblox_process(package_name)
                            time.sleep(2)
                            launch_roblox(package_name, server_link, num_packages, package_statuses)
                            executor_check_with_wait(username, package_name, package_statuses)
                        elif last_location_current == 'Website':
                            package_statuses[package_name]['Status'] = Fore.RED + 'On Website, Rejoining' + Style.RESET_ALL
                            kill_roblox_process(package_name)
                            time.sleep(2)
                            launch_roblox(package_name, server_link, num_packages, package_statuses)
                            executor_check_with_wait(username, package_name, package_statuses)
                        else:
                            package_statuses[package_name]['Status'] = Fore.YELLOW + 'Not In-Game, Recently Active' + Style.RESET_ALL
                        update_status_table(package_statuses)
                        time.sleep(25)

                    if executor_choice == '1':
                        for package_name, user_id in accounts:
                            bypass_results = bypass_user_ids(accounts, '1', minutes_left_dict)
                            for _, result in bypass_results:
                                minutes_left = result.get('minutesLeft', '0H 0M')
                                if minutes_left == '0H 0M':
                                    package_statuses[package_name]['Status'] = Fore.RED + 'Bypassing Now...' + Style.RESET_ALL
                                    update_status_table(package_statuses)
                                    bypass_user_ids(accounts, '1', minutes_left_dict)
                        update_status_table(package_statuses)

                    if executor_choice == '2' and current_time - last_bypass_time >= bypass_interval:
                        print('Performing Fluxus bypass operation...')
                        bypass_results = bypass_user_ids(accounts, '2')
                        last_bypass_time = current_time

                    time.sleep(90)

                    if current_time - start_time >= force_rejoin_interval:
                        print('Force killing Roblox processes due to time limit.')
                        kill_roblox_processes()
                        start_time = current_time
                        print(Fore.YELLOW + 'Waiting for 5 seconds before starting the rejoin process...' + Style.RESET_ALL)
                        time.sleep(5)
                        for package_name, server_link in server_links:
                            try:
                                package_statuses[package_name]['Status'] = Fore.RED + 'Rejoining' + Style.RESET_ALL
                                update_status_table(package_statuses)
                                launch_roblox(package_name, server_link, num_packages, package_statuses)
                                executor_check_with_wait(username, package_name, package_statuses)
                                package_statuses[package_name]['Status'] = Fore.GREEN + 'Joined' + Style.RESET_ALL
                            except Exception as e:
                                print(Fore.RED + 'Error rejoining Roblox for {}: {}'.format(package_name, e) + Style.RESET_ALL)
                        update_status_table(package_statuses)
            except Exception as e:
                print(Fore.RED + 'Critical error in bypass process: {}'.format(e) + Style.RESET_ALL)
                time.sleep(60)
                continue

        elif setup_type == '9':
            new_hwid = safe_input('Enter the new HWID you want to set for all Fluxus packages: ')
            packages = get_roblox_packages()
            for package_name in packages:
                hwid_file_path = get_hwid_file_path(package_name)
                if hwid_file_path:
                    try:
                        with open(hwid_file_path, 'w') as file:
                            file.write(new_hwid)
                        print(Fore.GREEN + 'HWID for {} successfully updated to {}'.format(package_name, new_hwid) + Style.RESET_ALL)
                    except Exception as e:
                        print(Fore.RED + 'Error updating HWID for {}: {}'.format(package_name, e) + Style.RESET_ALL)
                else:
                    print(Fore.RED + 'Failed to find HWID file for {}. Skipping.'.format(package_name) + Style.RESET_ALL)
            safe_input(Fore.GREEN + 'Press Enter to return to the menu...' + Style.RESET_ALL)

        elif setup_type == '10':
            inject_cookies_and_appstorage()
            safe_input(Fore.GREEN + 'Press Enter to exit...' + Style.RESET_ALL)

        elif setup_type == '11':
            logout_roblox()
            safe_input(Fore.GREEN + 'Press Enter to exit...' + Style.RESET_ALL)

        elif setup_type == '12':
            clear_console()
            print_header()
            print('----------------------------------------------------------------------')
            check_cookies_from_file('cookie.txt')
            safe_input(Fore.GREEN + 'Press Enter to exit...' + Style.RESET_ALL)

        elif setup_type == '13':
            setup_webhook()
            safe_input(Fore.GREEN + 'Press Enter to exit...' + Style.RESET_ALL)

        elif setup_type == '14':
            create_autoexc_folder()
            push_autoexc_files()
            safe_input(Fore.GREEN + 'Press Enter to exit...' + Style.RESET_ALL)

        elif setup_type == '15':
            os.system('cls' if os.name == 'nt' else 'clear')
            main_block_menu()
            safe_input(Fore.GREEN + 'Press Enter to exit...' + Style.RESET_ALL)

        elif setup_type == '16':
            clear_console()
            print_header()
            print('----------------------------------------------------------------------')
            process_accounts()
            safe_input(Fore.GREEN + 'Press Enter to exit...' + Style.RESET_ALL)

        elif setup_type == '17':
            clear_console()
            print_header()
            print('----------------------------------------------------------------------')
            getcookie_process()
            safe_input(Fore.GREEN + 'Press Enter to exit...' + Style.RESET_ALL)

        elif setup_type == '18':
            global stop_webhook_thread
            stop_webhook_thread = True
            break
if __name__ == '__main__':
    load_cache()
    delete_roblox_cache()
    main()
    save_cache()
