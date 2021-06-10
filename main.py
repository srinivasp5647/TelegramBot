import telegram
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# bot = telegram.Bot(token="1768456634:AAH9ZUnUIoO2oGeaoqRcgXrrNpture31Ces")

# # # print(bot.getMe())
# for msg in bot.getUpdates():
#     print(msg.message.text)

updater = Updater(token="1768456634:AAH9ZUnUIoO2oGeaoqRcgXrrNpture31Ces", use_context=True)
dispatcher = updater.dispatcher


# def start(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text='Hello there, I am a bot')
def start(update: Update, _: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}, How are you\!',
        
    )

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


def hey(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Hey, How can I help you!')

assist_handler = CommandHandler('hey', hey)
dispatcher.add_handler(assist_handler)


def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)


def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)




updater.start_polling()
updater.idle()
