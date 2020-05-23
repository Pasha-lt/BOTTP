import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from handlers import *
from settings import API_KEY, API_WEATHER

logging.basicConfig(format='%(asctime)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def main():
    mybot = Updater(API_KEY, use_context=True)

    logging.info("Loading.....")

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", start, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.contact, get_contact, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.location, get_weather, pass_user_data=True))

    mybot.start_polling()
    mybot.idle()
    logging.info("End.....")


if __name__ == '__main__':
    main()
