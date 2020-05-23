import sys
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from handlers import start, get_contact, get_weather
from settings import API_KEY

logging.basicConfig(format='%(asctime)s %(filename)25s:%(lineno)-4d %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%dT%H:%M:%S',
                    level=logging.INFO,
                    filename='bot.log',
                    )

console = logging.StreamHandler(sys.stdout)
console.setLevel(logging.INFO)
datefmt = '%Y-%m-%dT%H:%M:%S'
formatter = logging.Formatter('%(asctime)s %(filename)25s:%(lineno)-4d %(levelname)-8s %(message)s', datefmt=datefmt)
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
logger = logging.getLogger(__name__)


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
