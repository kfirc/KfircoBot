from os import path, environ
from dotenv import load_dotenv

from TelegramBot import TelegramBot

from handlers import setup_handlers


def load_and_validate_environment():
    # load environment from .env file
    basedir = path.abspath(path.dirname(__file__))
    load_dotenv(path.join(basedir, '.env'))

    for key in ('TELEGRAM_TOKEN', 'LOGGER_PATH'):
        if key not in environ:
            raise NotImplementedError(f"'{key}' environment variable isn't specified")


load_and_validate_environment()
bot = TelegramBot(
    token=environ['TELEGRAM_TOKEN'],
    logger_path=environ['LOGGER_PATH'],
    help_description="My name is KfirBot, I'm going to help you with everything you need!",
)
setup_handlers(bot)

if __name__ == '__main__':
    bot.start_polling()
