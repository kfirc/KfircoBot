from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Filters


def setup_handlers(bot):
    @bot.handle.message(Filters.command)
    def unknown(update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")
