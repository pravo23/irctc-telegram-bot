import os
from telebot import TeleBot

import rail_query_helper


BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start", "help"])
def greet(message):
    greet_message = """
    Welcome to the IRCTC Telegram Bot!
    Here are some commands you can use:
    */help* : Display help message
    */about* : Learn more about this bot
    */pnr* : Get the pnr status of the train ticket
    */searchStation* : Search station name
    */searchTrain* : Search the train by number
    */getFair* : Get fair for train
    */track* : Get train running status
    """
    bot.send_message(message.chat.id, greet_message, parse_mode='Markdown')


@bot.message_handler(commands=["pnr"])
def pnr_status(message):
    input_message = "Please Enter the PNR number!"
    sent_msg = bot.send_message(
        message.chat.id,
        input_message,
        parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, pnr_status_handler)


def pnr_status_handler(message):
    pnr_number = message.text
    status_msg = rail_query_helper.pnr_status_message(pnr_number)
    bot.send_message(message.chat.id, status_msg, parse_mode="Markdown")


@bot.message_handler(commands=["searchStation"])
def get_station(message):
    input_message = "Please enter the station code!"
    sent_message = bot.send_message(
        message.chat.id,
        input_message,
        parse_mode="Markdown")
    bot.register_next_step_handler(sent_message, get_station_handler)


def get_station_handler(message):
    station_code = message.text
    resp_message = rail_query_helper.search_station_response(station_code)
    bot.send_message(message.chat.id, resp_message, parse_mode="Markdown")


@bot.message_handler(commands=["searchTrain"])
def get_train(message):
    input_message = "Please enter the train number!"
    sent_message = bot.send_message(
        message.chat.id,
        input_message,
        parse_mode="Markdown")
    bot.register_next_step_handler(sent_message, get_train_handler)


def get_train_handler(message):
    train_code = message.text
    resp_message = rail_query_helper.search_train_response(train_code.strip())
    bot.send_message(message.chat.id, resp_message, parse_mode="Markdown")


@bot.message_handler(commands=["getFair"])
def get_fair(message):
    input_message = "Please enter the train number!"
    sent_message = bot.send_message(
        message.chat.id,
        input_message,
        parse_mode="Markdown")
    bot.register_next_step_handler(sent_message, get_source_station_code)


def get_source_station_code(message):
    train_code = message.text
    input_message = "Please Enter Source Station Code!"
    sent_message = bot.send_message(
        message.chat.id,
        input_message,
        parse_mode="Markdown"
    )
    bot.register_next_step_handler(
        sent_message,
        get_destination_station_code,
        train_code)


def get_destination_station_code(message, train_code):
    source_station_code = message.text.strip().upper()
    input_message = "Please Enter Destination Station Code!"
    sent_message = bot.send_message(
        message.chat.id,
        input_message,
        parse_mode="Markdown"
    )
    bot.register_next_step_handler(
        sent_message,
        get_fair_handler,
        train_code,
        source_station_code)


def get_fair_handler(message, train_code, source_station_code):
    dest_station_code = message.text.strip().upper()

    resp_message = rail_query_helper.fetch_fair_response(
        train_code, source_station_code, dest_station_code)
    bot.send_message(
        message.chat.id,
        resp_message,
        parse_mode="Markdown"
    )


@bot.message_handler(commands=["track"])
def get_train_running_status(message):
    input_message = "Please enter the train number!"
    sent_message = bot.send_message(
        message.chat.id,
        input_message,
        parse_mode="Markdown")
    bot.register_next_step_handler(
        sent_message, get_train_running_status_handler)


def get_train_running_status_handler(message):
    train_code = message.text
    resp_message = rail_query_helper.live_train_status_response(
        train_code.strip())
    bot.send_message(message.chat.id, resp_message, parse_mode="Markdown")


bot.infinity_polling()
