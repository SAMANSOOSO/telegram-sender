import time
import telebot

BOT_TOKEN = "PUT_YOUR_TOKEN_HERE"
CHAT_ID = "PUT_GROUP_ID_HERE"

MESSAGES = ["مرگ بر آمریکا", "مرگ بر اسرائیل"]

bot = telebot.TeleBot(BOT_TOKEN)

while True:
    for msg in MESSAGES:
        bot.send_message(CHAT_ID, msg)
        time.sleep(420)  # 7 minutes
