import logging
from telegram import Bot

TELEGRAM_BOT_TOKEN = '6907175148:AAGN4o_wIZcfyxgfJSbxdXuwtJpUbvlnfDU'
TELEGRAM_CHAT_ID = '846935339'

def send_telegram_notification(name, phone, email):
    print("Sending Telegram notification...")
    try:
        message = f"Новая заявка!\n\nИмя: {name}\nТелефон: {phone}\nEmail: {email}"
        bot = Bot(token=TELEGRAM_BOT_TOKEN)
        bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
        print("Telegram notification sent successfully!")
    except Exception as e:
        logging.error(f"Error sending Telegram notification: {e}")
        print(f"Error sending Telegram notification: {e}")