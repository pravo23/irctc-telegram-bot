import os
from telebot import TeleBot

import rail_query_helper


BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = TeleBot(BOT_TOKEN)

@bot.message_handler(commands=["start", "help"])
def greet(message):
    greet_message = "Hello, This a telegram app for  irctc train status"
    bot.send_message(message.chat.id, greet_message, parse_mode='Markdown')

@bot.message_handler(commands=["pnr"])
def pnr_status(message):
    input_message="Please Enter the PNR number!"
    sent_msg = bot.send_message(message.chat.id, input_message, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, pnr_status_handler)

def pnr_status_handler(message):
    pnr_number = message.text
    status_msg = rail_query_helper.pnr_status_message(pnr_number)
    bot.send_message(message.chat.id, status_msg, parse_mode="Markdown")



bot.infinity_polling()