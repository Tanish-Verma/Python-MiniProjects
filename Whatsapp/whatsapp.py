import pywhatkit
import datetime
import os
from dotenv import load_dotenv
load_dotenv()
PHONE_NUMBER = os.getenv("PHONE_NUMBER")

def send_whatsapp_message(phone_number, message, send_time=None):
    """
    Sends a WhatsApp message to the specified phone number.

    Parameters:
    phone_number (str): The recipient's phone number in international format (e.g., '+1234567890').
    message (str): The message to be sent.
    send_time (tuple, optional): A tuple containing hour and minute (24-hour format) to schedule the message.
                                 If None, the message is sent immediately.

    Returns:
    None
    """
    if send_time:
        hour, minute = send_time
        pywhatkit.sendwhatmsg(phone_number, message, hour, minute)
    else:
        current_time = datetime.datetime.now()
        pywhatkit.sendwhatmsg_instantly(phone_number, message)

send_whatsapp_message(PHONE_NUMBER, "Hello from Python!", send_time=(8, 20))