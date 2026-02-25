import os
import time
import requests

# Настройки
PLACE_ID = "142823291"
WEBHOOK_URL = "https://discord.com/api/webhooks/1475486473745862790/dtUDraerNlczUsq3pPUwZ-8-6xSuo4IFwMgHhtjQa0NPjdiQX6QFejTqxDHQANTiuvgn"
CHECK_INTERVAL = 30

def send_log(msg):
    print(msg)
    try: requests.post(WEBHOOK_URL, json={"content": f"📱 {msg}"})
    except: pass

def check_for_errors():
    # Дампим интерфейс в xml файл
    os.system("su -c 'uiautomator dump /sdcard/view.xml > /dev/null'")
    # Читаем файл и ищем ключевые слова ошибок Roblox
    try:
        with open("/sdcard/view.xml", "r") as f:
            ui_content = f.read()
            if "Disconnected" in ui_content or "Reconnect" in ui_content:
                return True
    except:
        pass
    return False

def restart_game():
    send_log("Обнаружена ошибка или вылет. Перезапуск...")
    # Убиваем процесс, чтобы зайти "на чистую"
    os.system("su -c 'am force-stop com.roblox.client'")
    time.sleep(2)
    # Запуск плейса
    os.system(f"su -c 'am start -a android.intent.action.VIEW -d \"roblox://placeID={PLACE_ID}\" com.roblox.client'")

if __name__ == "__main__":
    send_log("Мониторинг ошибок запущен.")
    while True:
        # 1. Проверка: запущен ли процесс
        is_running = "com.roblox.client" in os.popen("su -c 'ps -A | grep com.roblox.client'").read()
        
        if not is_running:
            restart_game()
        else:
            # 2. Проверка: нет ли окна ошибки поверх игры
            if check_for_errors():
                send_log("Найдено окно ошибки на экране!")
                restart_game()
        
        time.sleep(CHECK_INTERVAL)
