# =========================
# WhatsApp Message Scheduler
# =========================

from twilio.rest import Client
from datetime import datetime
import time
import os

# Load credentials from environment variables
ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

client = Client(ACCOUNT_SID, AUTH_TOKEN)


def send_whatsapp_message(recipient_number, message_body):
    try:
        message = client.messages.create(
            from_="whatsapp:+14874987486",  # Twilio Sandbox Number
            body=message_body,
            to=f"whatsapp:{recipient_number}"
        )

        print("✅ Message sent successfully")
        print("📨 Message SID:", message.sid)

    except Exception as e:
        print("❌ Error:", e)


# User Inputs
name = input("Enter the recipient name: ")
recipient_number = input(
    "Enter WhatsApp number with country code (e.g. +919876745610): "
)
message_body = input(f"Enter the message for {name}: ")

# Date & Time Inputs
date_str = input("Enter date (YYYY-MM-DD): ")
time_str = input("Enter time (HH:MM, 24-hour format): ")

scheduled_datetime = datetime.strptime(
    f"{date_str} {time_str}", "%Y-%m-%d %H:%M"
)

current_datetime = datetime.now()
delay_seconds = (scheduled_datetime - current_datetime).total_seconds()

if delay_seconds <= 0:
    print("❌ Time must be in the future")
else:
    print(f"⏳ Message scheduled for {scheduled_datetime}")
    time.sleep(delay_seconds)
    send_whatsapp_message(recipient_number, message_body)
