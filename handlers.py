import logging

from utils import get_keyboard
from weather import Weather


def start(update, context):
    logging.info(f"User {update.message.from_user} activate the bot")
    start_text = f"Hello {update.message.chat.first_name}"
    update.message.reply_text(start_text, reply_markup=get_keyboard())


def get_weather(update, context):
    logging.info(f"{update.message.from_user} send location {update.message.location.latitude} "
                 f"& {update.message.location.longitude}")
    weth = Weather(update.message.location.latitude, update.message.location.longitude).get_weather()
    response = f"Текущая температура {weth['temp_C']}, " \
               f"на улице {weth['lang_ru'][0]['value']}, " \
               f"ощущается на {weth['FeelsLikeC']} "
    update.message.reply_text(response, reply_markup=get_keyboard())


def get_contact(update, context):
    logging.info(f"User {update.message.chat.first_name} sends own contacts {update.message.contact}")
    update.message.reply_text(f"Спасибо!", reply_markup=get_keyboard())

