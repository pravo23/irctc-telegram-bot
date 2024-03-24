import os
from telebot import TeleBot

import rail_query_helper


BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = TeleBot(BOT_TOKEN)


def help_message():
    return """Available Commands:\n\n*/help* - Display a list of available commands.\n*/pnr* - Get the PNR status of a train ticket\n*/searchstation* -  Search for a station by name\n*/searchtrain* - Search for a train by number\n*/getfair* - Get fare information for a train\n*/track* - Track the running status of a train\n*/schedule* - Get the schedule time of a train\n*/trainbetweenstation* - Get the trains between stations"""


@bot.message_handler(commands=["start", "help"])
def greet(message):
    greet_message = "Welcome to the IRCTC Telegram Bot!\n\n" + help_message()
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
    bot.send_message(message.chat.id, help_message(), parse_mode="Markdown")


@bot.message_handler(commands=["searchstation"])
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
    bot.send_message(message.chat.id, help_message(), parse_mode="Markdown")


@bot.message_handler(commands=["searchtrain"])
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
    bot.send_message(message.chat.id, help_message(), parse_mode="Markdown")


@bot.message_handler(commands=["getfair"])
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
    bot.send_message(message.chat.id, help_message(), parse_mode="Markdown")


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
    bot.send_message(message.chat.id, help_message(), parse_mode="Markdown")


@bot.message_handler(commands=["schedule"])
def get_train_schedule(message):
    input_message = "Please enter the train number!"
    sent_message = bot.send_message(
        message.chat.id,
        input_message,
        parse_mode="Markdown")
    bot.register_next_step_handler(
        sent_message, get_train_schedule_handler)


def get_train_schedule_handler(message):
    train_code = message.text
    resp_message = rail_query_helper.train_schedule_response(
        train_code.strip())
    bot.send_message(message.chat.id, resp_message, parse_mode="Markdown")
    bot.send_message(message.chat.id, help_message(), parse_mode="Markdown")


@bot.message_handler(commands=["trainbetweenstation"])
def get_train_between_station_source(message):
    input_message = "Please enter the *station-code* for source station!"
    sent_message = bot.send_message(
        message.chat.id,
        input_message,
        parse_mode="Markdown")
    bot.register_next_step_handler(
        sent_message, get_train_between_station_destination)


def get_train_between_station_destination(message):
    source_station = message.text
    input_message = "Please enter the *station-code* for destination station!"
    sent_message = bot.send_message(
        message.chat.id,
        input_message,
        parse_mode="Markdown")
    bot.register_next_step_handler(
        sent_message,
        get_train_between_station_date,
        source_station)


def get_train_between_station_date(message, source_station):
    destination_station = message.text
    input_message = "Please enter the *date* in format YYYY-MM-DD!"
    sent_message = bot.send_message(
        message.chat.id,
        input_message,
        parse_mode="Markdown")
    bot.register_next_step_handler(
        sent_message,
        get_train_between_station_handler,
        source_station,
        destination_station)


def get_train_between_station_handler(
        message,
        source_station,
        destination_station):
    date = message.text.strip()
    source_station = source_station.strip().upper()
    destination_station = destination_station.strip().upper()

    resp_message = rail_query_helper.train_between_station_response(
        source_station, destination_station, date)
    bot.send_message(message.chat.id, resp_message, parse_mode="Markdown")
    bot.send_message(message.chat.id, help_message(), parse_mode="Markdown")


bot.infinity_polling()
