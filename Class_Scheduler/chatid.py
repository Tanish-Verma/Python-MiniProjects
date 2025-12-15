import requests
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN  = os.getenv("BOT_TOKEN")

url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"

data = requests.get(url=url).json()

# print(data.get("result"))
if data.get("ok") and data.get("result"):

    first_update = data["result"][0]
    message_object = first_update.get("message")

    if message_object:
        chat_object = message_object.get("chat")
        
        if chat_object:
            chat_id = chat_object.get("id")
            
            if chat_id is not None:
                print(f"The first chat ID is: {chat_id}")
            else:
                print("Could not find 'id' within the 'chat' object.")
        else:
            print("Could not find 'chat' object within the message.")
    else:
        print("No new message or edited message found in the first update.")
else:
    # This might happen if 'ok' is false (API error) or 'result' is empty (no new updates)
    print("Request failed or no updates received.")
