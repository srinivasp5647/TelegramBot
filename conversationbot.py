import re
from threading import TIMEOUT_MAX

from telegram.error import TimedOut
from conversationbot2 import CHOOSING, TYPING_CHOICE, TYPING_REPLY
import logging
import sample as S
from telegram import *   
from telegram.ext import * 
import time
import pdb


logging.basicConfig(
    format= '%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

CHOOSING, TYPING_CHOICE, TYPING_REPLY = range(3)

reply_keyboard = [
    ['Yes', 'No'],
    ['Done'],      
]
reply_keyboard1 = [
    ['Bit Mart', 'Different one']
]

reply_keyboard2 = [
    ['I have some experience', 'Not so much, but I want to learn']
]

reply_keyboard3 = [
    ['Yes, I had some issues', 'No. Everything went smoothly']
]

reply_keyboard4 = [
    ['Okay', 'Not Okay']
]

reply_keyboard5 = [
    ['Interested', 'Not Interested']
]

reply_keyboard6 = [
    ['Yes, please', 'No, thanks']
]
reply_keyboard7 = [
    ['I would like to', 'Not now']
]
reply_keyboard8 = [
    ['Happy to', 'Another time']
]

markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
markup1 = ReplyKeyboardMarkup(reply_keyboard1, one_time_keyboard=True)
markup2 = ReplyKeyboardMarkup(reply_keyboard2, one_time_keyboard=True)
markup3 = ReplyKeyboardMarkup(reply_keyboard3, one_time_keyboard=True)
markup4 = ReplyKeyboardMarkup(reply_keyboard4, one_time_keyboard=True)
markup5 = ReplyKeyboardMarkup(reply_keyboard5, one_time_keyboard=True)
markup6 = ReplyKeyboardMarkup(reply_keyboard6, one_time_keyboard=True)
markup7 = ReplyKeyboardMarkup(reply_keyboard7, one_time_keyboard=True)
markup8 = ReplyKeyboardMarkup(reply_keyboard8, one_time_keyboard=True)


def start(update: Update, context: CallbackContext) -> int:
    try:
        update.message.reply_text(
            "Hi there and welcome to Fly")
        
        update.message.reply_text(
            "Have you purchased from us before?",
            reply_markup = markup,
        )
        return CHOOSING
    except:
        update.message.reply_text(
            "Hi there and welcome to Fly")
        
        update.message.reply_text(
            "Have you purchased from us before?",
            reply_markup = markup,
        )
        return CHOOSING



def fly_yes(update: Update, context: CallbackContext) -> int:
    try:
        user = update.message.from_user
        logger.info(f"{user.first_name} purchased fly coin")
        update.message.reply_text(
            "Great! And which portals did you use ?",
            reply_markup = markup1,
        )
        return CHOOSING
    except:
        user = update.message.from_user
        logger.info(f"{user.first_name} purchased fly coin")
        update.message.reply_text(
            "Great! And which portals did you use ?",
            reply_markup = markup1,
        )
        return CHOOSING



def bit_portal(update: Update, context: CallbackContext) -> int:
    try:
        logger.info("-----try------")
        text = update.message.text
        context.user_data['choice'] = text
        update.message.reply_text(
            "Yes that's one of our popular online portals for FLY Token\ntell me please, did you experience any issues when purchasing?",
            reply_markup=markup3,
            )
        return CHOOSING
    except:
        logger.info("-----except------")
        text = update.message.text
        context.user_data['choice'] = text
        update.message.reply_text(
            "Yes that's one of our popular online portals for FLY Token\ntell me please, did you experience any issues when purchasing?",
            reply_markup=markup3,
            )
        return CHOOSING

def diff_portal(update: Update, context: CallbackContext) -> int:
    try:
        update.message.reply_text(
            "That's great to hear!",
            reply_markup=markup3,
        )
        return CHOOSING
    except:
        update.message.reply_text(
            "That's great to hear!",
            reply_markup=markup3,
        )
        return CHOOSING

def issue(update: Update, context: CallbackContext) -> int:
    try:
        update.message.reply_text(
            "I am sorry to hear that.\nWould you be okay with sharing some more information regarding the issues you faced?",
            reply_markup=markup7,
        )

        return CHOOSING
    except:
        update.message.reply_text(
            "I am sorry to hear that.\nWould you be okay with sharing some more information regarding the issues you faced?",
            reply_markup=markup7,
        )

        return CHOOSING
    

def no_issue(update: Update, context: CallbackContext) -> int:
    try:
        update.message.reply_text(
            "I am glad to hear"
        )
        update.message.reply_text(
            "Before I say goodbye to you, can I sign you up for our monthly newsletter?\nIt's packed with all of the latest cryptocurrency tips.",
            reply_markup=markup6,
        )
    except:
        update.message.reply_text(
            "I am glad to hear"
        )
        update.message.reply_text(
            "Before I say goodbye to you, can I sign you up for our monthly newsletter?\nIt's packed with all of the latest cryptocurrency tips.",
            reply_markup=markup6,
        )

def feedback(update: Update, context: CallbackContext) -> int:
    try:
        update.message.reply_text(
            "Please, explain us the issue",
            reply_markup=ReplyKeyboardRemove(),
        )
        return TYPING_REPLY
        
    except:
        update.message.reply_text(
            "Please, explain us the issue",
            reply_markup=ReplyKeyboardRemove(),
        )
        return TYPING_REPLY
        

def received_information(update: Update, context: CallbackContext) -> int:
    try:
        update.message.reply_text(
            "Thank you, your feedback is highly appreicated.",
            reply_markup=ReplyKeyboardRemove(),
        )
        return ConversationHandler.END
    except:
        update.message.reply_text(
            "Thank you, your feedback is highly appreicated.",
            reply_markup=ReplyKeyboardRemove(),
        )
        return ConversationHandler.END


def no_feedback(update: Update, context: CallbackContext) -> int:
    try:
        update.message.reply_text(
            "We are sorry to hear that, if you would like any help please reach out to us.",
            reply_markup=ReplyKeyboardRemove(),
        )
        return ConversationHandler.END
    except:
        update.message.reply_text(
            "We are sorry to hear that, if you would like any help please reach out to us.",
            reply_markup=ReplyKeyboardRemove(),
        )
        return ConversationHandler.END

def newsletter(update: Update, context: CallbackContext) -> int:
    try:
        update.message.reply_text(
            "Great! All that I need to get you in, is your email address",
            reply_markup=ReplyKeyboardRemove(),
        )
        return TYPING_CHOICE
    except:
        update.message.reply_text(
            "Great! All that I need to get you in, is your email address",
            reply_markup=ReplyKeyboardRemove(),
        )
        return TYPING_CHOICE

def no_newsletter(update: Update, context: CallbackContext) -> int:
    try:
        update.message.reply_text(
            "No problem.\nHave a good day",
            reply_markup=ReplyKeyboardRemove(),
        )
        return ConversationHandler.END
    except:
        update.message.reply_text(
            "No problem.\nHave a good day",
            reply_markup=ReplyKeyboardRemove(),
        )
        return ConversationHandler.END


def success(update: Update, context: CallbackContext) -> int:
    try:
        update.message.reply_text(
            "Well Done! You are all signed up!\nHope you have a great day!",
            reply_markup=ReplyKeyboardRemove(),
        )
        return ConversationHandler.END
    except:
        update.message.reply_text(
            "Well Done! You are all signed up!\nHope you have a great day!",
            reply_markup=ReplyKeyboardRemove(),
        )
        return ConversationHandler.END

def no_fly(update: Update, context: CallbackContext) -> int:
    try:
        user = update.message.from_user
        logger.info(f"{user.first_name} not purchased Fly coin")
        update.message.reply_text(
            "Ok and are you interested in finding out more about Fly coin ?",
            reply_markup=markup5,
        )
        return CHOOSING
    except:
        user = update.message.from_user
        logger.info(f"{user.first_name} not purchased Fly coin")
        update.message.reply_text(
            "Ok and are you interested in finding out more about Fly coin ?",
            reply_markup=markup5,
        )
        return CHOOSING


def not_interest(update: Update, context: CallbackContext) -> int:
    try:
        update.message.reply_text(
            "That's fine, thank you for your time.\nIf would like to discuss anything else feel free to message us!\nUntil next time.",
            reply_markup=ReplyKeyboardRemove(),
        )
        return ConversationHandler.END
    except:
        update.message.reply_text(
            "That's fine, thank you for your time.\nIf would like to discuss anything else feel free to message us!\nUntil next time.",
            reply_markup=ReplyKeyboardRemove(),
        )
        return ConversationHandler.END

def interested(update: Update, context: CallbackContext) -> int:
    try:
        update.message.reply_text(
            'Great!So how familiar are you with cryptocurrencies?',
            reply_markup=markup2,
        )
        return CHOOSING
    except:
        update.message.reply_text(
            'Great!So how familiar are you with cryptocurrencies?',
            reply_markup=markup2,
        )
        return CHOOSING

def experience(update: Update, context: CallbackContext) -> int:
    try:
        update.message.reply_text(
            "That's good to hear. Well a great first start would be to visit\nour FLY portal website.\nThis will provid easy access to purchase our Fly token -  https://tokenfly.co"
        )
        update.message.reply_text(
            'Are you happy to proceed?',
            reply_markup=markup8,
        )
    except:
        update.message.reply_text(
            "That's good to hear. Well a great first start would be to visit\nour FLY portal website.\nThis will provid easy access to purchase our Fly token -  https://tokenfly.co"
        )
        update.message.reply_text(
            'Are you happy to proceed?',
            reply_markup=markup8,
        )


def proceed(update: Update, context: CallbackContext) -> int:
    try:
        update.message.reply_text(
            "Great and best of luck with your endeavours.\nThanks again for joining us.",
            reply_markup=ReplyKeyboardRemove(),
        )
        return ConversationHandler.END
    except:
        update.message.reply_text(
            "Great and best of luck with your endeavours.\nThanks again for joining us.",
            reply_markup=ReplyKeyboardRemove(),
        )
        return ConversationHandler.END

def not_proceed(update: Update, context: CallbackContext) -> int:
    try:
        update.message.reply_text(
            "That's fine, thank you for your time, if you would like some more information or have any questions feel free to message us.",
            reply_markup=ReplyKeyboardRemove(),
        )
        return ConversationHandler.END
    except:
        update.message.reply_text(
            "That's fine, thank you for your time, if you would like some more information or have any questions feel free to message us.",
            reply_markup=ReplyKeyboardRemove(),
        )
        return ConversationHandler.END


def not_exp(update: Update, context: CallbackContext) -> int:
    try:
        update.message.reply_text(
            "No worries, we're here to help you! Would you like to receive some newsletters with the latest crypto news and tips?",
            reply_markup=markup6,
        )
    except:
        update.message.reply_text(
            "No worries, we're here to help you! Would you like to receive some newsletters with the latest crypto news and tips?",
            reply_markup=markup6,
        )


def done(update: Update, context: CallbackContext) -> int:
    try:
        user_data = context.user_data
        update.message.reply_text(
            "Until next time!\nBye",
            reply_markup=ReplyKeyboardRemove(), 
        )
        user_data.clear()
        return ConversationHandler.END
    except:
        user_data = context.user_data
        update.message.reply_text(
            "Until next time!\nBye",
            reply_markup=ReplyKeyboardRemove(), 
        )
        user_data.clear()
        return ConversationHandler.END

def new():
    print("-------1---------")
    updater = Updater(S.API_KEY, use_context= True)
    
    print("------2----------")

    dp = updater.dispatcher
    print("------3----------")
    conv_handler = ConversationHandler(
        entry_points=[MessageHandler(Filters.text, start)],
        states = {
            CHOOSING: [
                MessageHandler(Filters.regex('^Yes$'), fly_yes),
                MessageHandler(Filters.regex('^Bit Mart$'), bit_portal),
                MessageHandler(Filters.regex('^Different one$'), diff_portal),
                MessageHandler(Filters.regex('^Yes, I had some issues$'), issue),
                MessageHandler(Filters.regex('^No. Everything went smoothly$'), no_issue),
                MessageHandler(Filters.regex('^I would like to$'), feedback),
                MessageHandler(Filters.regex('^Not now$'), no_feedback),
                MessageHandler(Filters.regex('^Yes, please$'), newsletter),
                MessageHandler(Filters.regex('^No, thanks$'), no_newsletter),
                MessageHandler(Filters.regex('^No$'), no_fly),
                MessageHandler(Filters.regex('^Interested$'), interested),
                MessageHandler(Filters.regex('^Not Interested$'), not_interest),
                MessageHandler(Filters.regex('^I have some experience$'), experience),
                MessageHandler(Filters.regex('^Happy to$'), proceed),
                MessageHandler(Filters.regex('^Another time$'), not_proceed),
                MessageHandler(Filters.regex('^Not so much, but i want to learn$'), not_exp),
                MessageHandler(Filters.regex('^Done$'), done),
            ],
            TYPING_CHOICE: [
                
                MessageHandler(Filters.text, success)
            ],
            TYPING_REPLY: [
                MessageHandler(Filters.text & ~(Filters.command) ,received_information)
            ],
        },
        fallbacks=[MessageHandler(Filters.regex('^Done$'), done)],
        
    )
    print("-------4---------")

    dp.add_handler(conv_handler)
    print("-------5---------")
    # dp.add_error_handler(new)
    updater.start_polling()
    print("--------6--------")
    updater.idle()


def main() -> None:
    new()
    


if __name__ == '__main__':
    main()

