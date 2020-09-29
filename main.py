from os import path
from dotenv import load_dotenv

from TelegramBot import TelegramBot

from handlers import setup_handlers

# load environment from .env file
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

bot = TelegramBot(
    help_description="My name is KfirBot, I'm going to help you with everything you need!"
)
setup_handlers(bot)

if __name__ == '__main__':
    bot.start_polling()
