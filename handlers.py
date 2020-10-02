from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Filters

from globals import owner


def setup_handlers(bot):

    @bot.handle.command()
    def start(update, context):
        user = update.message.from_user
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"Hello {user['first_name']}, my name is KfirBot, how can I help you?",
        )
        bot.help(update, context)

    @bot.handle.message(Filters.text & (~Filters.command))
    def echo(update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

    @bot.handle.command()
    def details(update, context):
        """Receive some personal details about the owner"""
        context.bot.send_message(chat_id=update.effective_chat.id, text=str(owner))

    @bot.handle.command()
    def caps(update, context):
        """Will return everything in caps"""

        text_caps = ' '.join(context.args).upper() or '...'
        context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

    @bot.handle.inline_query()
    def inline_caps(update, context):
        query = update.inline_query.query
        if not query:
            return
        results = list()
        results.append(
            InlineQueryResultArticle(
                id=query.upper(),
                title='Caps',
                input_message_content=InputTextMessageContent(query.upper())
            )
        )
        context.bot.answer_inline_query(update.inline_query.id, results)

    @bot.handle.message(Filters.command)
    def unknown(update, context):
        user = update.message.from_user
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"Sorry {user['first_name']}, I didn't understand your command.\nUse /help for guidance.",
        )
