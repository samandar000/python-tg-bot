import os
import json
from telegram import Update,ReplyKeyboardMarkup
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackContext,
    MessageHandler,
    filters
)

TOKEN = os.environ['TOKEN']

keyboard = [
    ['👍', '👎']
]
def chat_id(update:Update):
    chat_id = update.message.chat.id
    with open('data.json') as f:
        data = json.loads(f.read())
    with open('data.json') as f:
        f.write(chat_id)
        f.write(json.dumps(chat_id,indent=4))
def increase_like():
    with open('data.json') as f:
        data = json.loads(f.read())
        data['likes'] += 1    
    with open('data.json') as f:
        f.write('')
        f.write(json.dumps(data,indent=4))
    return data['likes'],data['dislikes']

def increase_dislike():
    with open('data.json') as f:
        data = json.loads(f.read())
        data['dislikes'] += 1
    with open('data.json', 'w') as f:
        f.write('')
        f.write(json.dumps(data, indent=4))
    
    return data['likes'], data['dislikes']

def start(update: Update, context: CallbackContext):
    update.message.reply_html(text="<b>Assalomu alaylum!</b>\n\n<i>like botga xush kelibsiz!!</i>", \
        reply_markup=ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True))

def like(update: Update, context: CallbackContext):
    likes, dislikes = increase_like()
    update.message.reply_html(text=f"<b>like:</b> {likes}\n<b>dislike:</b> {dislikes}", \
        reply_markup=ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True))

def dislike(update: Update, context: CallbackContext):
    likes, dislikes = increase_dislike()
    update.message.reply_html(text=f"<b>like:</b> {likes}\n<b>dislike:</b> {dislikes}", \
        reply_markup=ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True))

def default(update: Update, context: CallbackContext):
    update.message.reply_html(text="iltimos buttonlardan birini bosing!", \
        reply_markup=ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True))

def main():
    updater = Updater(token=TOKEN)
    dp = updater.dispatcher

    dp.add_handler(handler=CommandHandler(command='start',callback=start))

    dp.add_handler(handler=MessageHandler(filters=filters.Filters.text('👍'), callback=like))
    dp.add_handler(handler=MessageHandler(filters=filters.Filters.text('👎'), callback=dislike))

    dp.add_handler(handler=MessageHandler(filters=filters.Filters.all, callback=default))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()         