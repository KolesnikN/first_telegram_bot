from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
import random
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from my_token import token

isFriendly = True
moods = ["happy", "sad", "ok", "bored"] # moods for "How are you" func

def start_message (update: Update, context: CallbackContext):
    reply_markup = ReplyKeyboardMarkup(
        [
            [KeyboardButton('Hi'), KeyboardButton('How are you?')]
        ]
    )
    context.bot.send_message(update.message.chat.id, """
        Hi! I am test bot. You can write Hi or ask How are you.
    """, reply_markup=reply_markup)

def hi_message(update: Update):
    if (not isFriendly): return
    update.message.reply_text("Hi! I am very glad to see you")

def how_message(update: Update):
    mood = random.choice(moods)
    update.message.reply_text("I am {}".format(mood))
# Select message bsed on input
def selector (update: Update, context: CallbackContext):
    text = update.message.text
    if (text == 'Hi'):
        hi_message(update)
    elif (text == 'How are you?'):
        how_message(update)

updater = Updater(token)

dispatcher = updater.dispatcher
# Add handlers
dispatcher.add_handler(CommandHandler(['start', 'help'], start_message))
dispatcher.add_handler(MessageHandler(Filters.text, selector))
# checking for input and stop flow
updater.start_polling()

updater.idle()