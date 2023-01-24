import os
from telegram.ext import Updater,MessageHandler,filters,CallbackContext,CommandHandler,BaseFilter
from telegram import Update,ReplyKeyboardMarkup
import requests

TOKEN = os.environ['TOKEN']

def start(update: Update,context:CallbackContext):
    keyboard = [['dog'],['cat']]
    update.message.reply_text('Welcome to our bot',reply_markup=ReplyKeyboardMarkup(keyboard=keyboard))

def cat(update: Update, context: CallbackContext):
    response = requests.get('https://aws.random.cat/meow')
    url = response.json()['file']

    update.message.reply_photo(url)

def dog(update: Update, context: CallbackContext):
    response = requests.get('https://random.dog/woof.json')
    url = response.json()['url']

    update.message.reply_photo(url)


def main():

    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(handler=CommandHandler('start', callback=start))

    
    dispatcher.add_handler(handler=MessageHandler(filters=filters.Filters.text('dog'),callback=dog))
    dispatcher.add_handler(handler=MessageHandler(filters=filters.Filters.text('cat'),callback=cat))

    
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":    
    main()