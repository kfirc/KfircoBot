from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Filters

from globals import owner


def setup_handlers(bot):

    @bot.handle.command()
    def start(update, context):
        user = update.message.from_user
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"Hello {user['first_name']}, my name is KfircoBot, how can I help you?",
        )
        bot.help(update, context)

    @bot.handle.message(Filters.text & (~Filters.command))
    def echo(update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

    @bot.handle.command()
    @bot.handle.callback_query()
    def menu(update, context):
        """ Opens up the main menu """

        update_message_text = update.callback_query.edit_message_text if update.callback_query else update.message.reply_text
        update_message_text(
            text='Please choose an option.',
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton('Author Details', callback_data='details'),
                    InlineKeyboardButton('Help', callback_data='help'),
                ],
                [
                    InlineKeyboardButton('Linkedin Profile', url=owner.website),
                    InlineKeyboardButton('Github repo', url='https://github.com/kfirc/KfircoBot'),
                ],
            ]),
        )

    @bot.handle.command()
    @bot.handle.callback_query()
    def details(update, context):
        """Receive some personal details about the owner"""
        context.bot.send_message(chat_id=update.effective_chat.id, text=str(owner))

    @bot.handle.message(Filters.command)
    def unknown(update, context):
        user = update.message.from_user
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"Sorry {user['first_name']}, I didn't understand your command.\nUse /help for guidance.",
        )
