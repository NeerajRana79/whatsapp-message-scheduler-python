WhatsApp Message Scheduler using Python 🚀

A Python-based automation project that allows users to schedule WhatsApp messages for a future date and time using the Twilio WhatsApp API.
This project demonstrates real-world concepts such as API integration, task scheduling, environment variables, and secure credential management.

✨ Features

📅 Schedule WhatsApp messages for a specific date & time

💬 Send WhatsApp messages using Twilio API

🔐 Secure credential handling using environment variables

🧠 Beginner-friendly and well-structured Python code

⚠️ Proper error handling and clear console logs

🛠️ Technologies Used

Python 3

Twilio WhatsApp API

datetime module

time module

Git & GitHub

📂 Project Structure
whatsapp-message-scheduler-python/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
📦 Installation
1️⃣ Clone the Repository
git clone https://github.com/NeerajRana79/whatsapp-message-scheduler-python.git
cd whatsapp-message-scheduler-python
2️⃣ Install Dependencies
pip install -r requirements.txt
🔐 Environment Variables (IMPORTANT)

For security reasons, Twilio credentials are NOT hardcoded in the source code.

Set the following environment variables:

🪟 Windows (PowerShell)
setx TWILIO_ACCOUNT_SID "your_account_sid_here"
setx TWILIO_AUTH_TOKEN "your_auth_token_here"
🐧 macOS / Linux
export TWILIO_ACCOUNT_SID="your_account_sid_here"
export TWILIO_AUTH_TOKEN="your_auth_token_here"
📱 Twilio WhatsApp Sandbox Setup

Create a Twilio account at: https://www.twilio.com

Go to Messaging → Try it out → WhatsApp Sandbox

From your WhatsApp, send:

join <sandbox-code>

to:

+14155238886

⚠️ This step is required to send WhatsApp messages in trial mode.

▶️ How to Run the Project
python main.py
Sample Input
Enter the recipient name: Neeraj
Enter WhatsApp number with country code: +919XXXXXXXXX
Enter the message: Hello, this message is scheduled!
Enter date (YYYY-MM-DD): 2026-02-21
Enter time (HH:MM): 22:07
🔒 Security Best Practices Used

❌ No credentials stored in source code

✅ Uses environment variables

✅ .env and sensitive files ignored via .gitignore

✅ Compatible with GitHub secret scanning
