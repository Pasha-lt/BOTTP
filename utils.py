import logging

from telegram import KeyboardButton, ReplyKeyboardMarkup


log = logging.getLogger(__name__)


def get_keyboard():
    contact_button = KeyboardButton("Прислать контакты", request_contact=True)
    location_button = KeyboardButton("Узнать погоду", request_location=True)
    my_keyboard = ReplyKeyboardMarkup([["To be done", "To be done"],
                                       [contact_button, location_button]
                                       ], resize_keyboard=True
                                      )
    return my_keyboard
