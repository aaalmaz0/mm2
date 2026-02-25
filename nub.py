import os
import time
import requests
import subprocess

# --- НАСТРОЙКИ ---
PLACE_ID = "142823291"
WEBHOOK_URL = "https://discord.com/api/webhooks/1475486473745862790/dtUDraerNlczUsq3pPUwZ-8-6xSuo4IFwMgHhtjQa0NPjdiQX6QFejTqxDHQANTiuvgn"
CHECK_INTERVAL = 15
TARGET_COLOR = "353a3b" # Твой цвет ошибки

def send_log(msg):
    print(msg)
    try: requests.post(WEBHOOK_URL, json={"content": f"🛡️ **Roblox Guard**: {msg}"})
    except: pass

def check_error_screen():
    """Проверяет наличие цвета ошибки в центре экрана"""
    # Делаем маленький скриншот центра (100x100 пикселей) для экономии ресурсов
    # Команда берет дамп экрана и вытягивает HEX цвета
    cmd = "su -c 'screencap | hexdump -C | grep \"35 3a 3b\"'"
    result = subprocess.getoutput(cmd)
    return TARGET_COLOR in result.replace(" ", "")

def restart_game(reason):
    send_log(f"Перезапуск: {reason}")
    os.system("su -c 'am force-stop com.roblox.client'")
    time.sleep(2)
    os.system(f"su -c 'am start -a android.intent.action.VIEW -d \"roblox://placeID={PLACE_ID}\" com.roblox.client'")

if __name__ == "__main__":
    send_log("Мониторинг по цвету #353a3b запущен.")
    while True:
        # 1. Проверка: запущен ли процесс
        is_running = "com.roblox.client" in os.popen("su -c 'ps -A | grep com.roblox.client'").read()
        
        if not is_running:
            restart_game("Игра закрыта")
        else:
            # 2. Проверка: висит ли окно ошибки
            if check_error_screen():
                restart_game("Найдено окно ошибки (Disconnected)")
        
        time.sleep(CHECK_INTERVAL)
