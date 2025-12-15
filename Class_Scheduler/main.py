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

def getTimetable(today):

    text = ""
    day_timetable = Timetable.timetable.get(today)
    for key,classes in day_timetable.items():
        if classes!= None:
            # print(classes)
            course = classes.get('Course')
            classroom = classes.get('Classroom')
            # print(course,classroom)
            text += f"- {course} - {key} - {classroom}\n"
    return text

def SendTimetable():
    try:
        today = datetime.datetime.now().strftime('%A')
        text = ""
        today_schedule = Timetable.timetable.get(today, ["No Classes Today"])
        if today_schedule == ["No Classes Today"]:
            text = today_schedule[0]
        else:  
            text = f"<b>Today's Timetable ({today})</b>\n\n"
            text += f'{getTimetable(today)}'
            text+= "\n\nHave a nice day"

        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        params = {
            "chat_id": CHAT_ID,
            "text": text,
            "parse_mode": "HTML"
        }

        requests.get(url, params=params)
        print("Sent timetable for:", today)

    except Exception as e:
        print(f"Failed to upload Timetable ,{e}")



if __name__ == "__main__":
    # schedule.every().day.at("07:00").do(SendTimetable)
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)
    SendTimetable()


