from TelegramBot import TelegramBot
from config import Config
from handlers import setup_handlers


bot = TelegramBot(token=Config.TELEGRAM_TOKEN, logger_path=Config.LOGGER_PATH)
setup_handlers(bot)

if __name__ == '__main__':
    bot.start_polling()
