import os
import time
import requests

# Настройки
PLACE_ID = "142823291"
WEBHOOK_URL = "https://discord.com/api/webhooks/1475486473745862790/dtUDraerNlczUsq3pPUwZ-8-6xSuo4IFwMgHhtjQa0NPjdiQX6QFejTqxDHQANTiuvgn"
CHECK_INTERVAL = 10

def send_discord_log(message):
    try:
        data = {"content": f"🚀 **Roblox Monitor**: {message}"}
        requests.post(WEBHOOK_URL, json=data)
    except Exception as e:
        print(f"Ошибка отправки в Discord: {e}")

def check_and_restart():
    # Проверка процесса через root shell
    check = os.popen("su -c 'ps -A | grep com.roblox.client'").read()
    
    if "com.roblox.client" not in check:
        print("Roblox закрыт. Перезапуск...")
        send_discord_log(f"Игра вылетела! Перезахожу в плейс `{PLACE_ID}`")
        
        # Команда запуска
        launch_cmd = f"su -c 'am start -a android.intent.action.VIEW -d \"roblox://placeID={PLACE_ID}\" com.roblox.client'"
        os.system(launch_cmd)

# Перед запуском установите библиотеку: pip install requests
if __name__ == "__main__":
    print("Мониторинг запущен...")
    send_discord_log("Скрипт мониторинга успешно запущен на телефоне.")
    while True:
        check_and_restart()
        time.sleep(CHECK_INTERVAL)
