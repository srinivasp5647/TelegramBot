
from logging import Filter
import sample as S
from telegram import *
from telegram.ext import *

print('Bot started...')

def start_command(update, context):
    user = update.effective_user
    update.message.reply_markdown_v2(fr'Hi {user.mention_markdown_v2()}, Welcome\!/n what can i do for you ')


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = S.message_response(text)

    update.message.reply_text(response)


# def echo(update, context):
#     update.message.reply_text(update.message.text)


def main():

    updater = Updater(S.API_KEY, use_context= True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start_command))
    # dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    

    updater.start_polling()
    updater.idle()


main()