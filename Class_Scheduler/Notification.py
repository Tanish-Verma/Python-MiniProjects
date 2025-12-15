import requests
import Timetable
import schedule
import time
import datetime
import os
from dotenv import load_dotenv  

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")  

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

def send_message():
    """Send a Telegram message indicating ride status check."""
    if not BOT_TOKEN or not CHAT_ID:
        print(f"[{datetime.datetime.now()}] BOT_TOKEN or CHAT_ID not set; skipping send.")
        return
    text = "Check on Aunty ride status"
    params = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "HTML"
    }
    try:
        resp = requests.get(url, params=params, timeout=10)
        if resp.ok:
            print(f"[{datetime.datetime.now()}] Message sent successfully.")
        else:
            print(f"[{datetime.datetime.now()}] Failed to send message: {resp.status_code} {resp.text}")
    except Exception as e:
        print(f"[{datetime.datetime.now()}] Exception while sending message: {e}")

# Schedule the job every 15 minutes
schedule.every(3).minutes.do(send_message)

if __name__ == "__main__":
    # Optionally send one immediately on start
    send_message()
    print(f"[{datetime.datetime.now()}] Scheduler started: sending every 15 minutes.")
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"[{datetime.datetime.now()}] Scheduler stopped by user.")
