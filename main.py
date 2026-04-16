import telebot
import os
from logic import ImgAPI

API_TOKEN = ''

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def generate_picture(message):
    api = ImgAPI()
    promt = message.text
    result = api.download_image(promt)
    with open(result, "rb") as photo:
        bot.send_document(message.chat.id, photo)
    os.remove(result)

bot.infinity_polling()
