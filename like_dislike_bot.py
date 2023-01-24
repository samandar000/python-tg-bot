from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
import json



def start(update, context):
    chat_id = update.message.chat.id
    bot = context.bot

    bot.sendMessage(chat_id, 'Welcome!')

def echo(update, context):
    chat_id = update.message.chat.id
    text = update.message.text
    bot = context.bot
    
   
    f = open('data.json').read()
    data = json.loads(f)
    
    like = data.get('LIKE')
    dislike = data.get('DISLIKE')
    if text == '👍':
        like+=1
    if text == '👎':
        dislike+=1
    
    data['LIKE'] = like
    data['DISLIKE'] = dislike
    data = json.dumps(data)
    f = open('data.json','w')
    f.write(data)
    f.close()
    if text != '👎' and text != '👍':
        bot.sendMessage(chat_id, text)
    else:
        bot.sendMessage(chat_id,f"👍:{like}\n\n👎:{dislike}")
        


    


    
updater = Updater("5643654386:AAGaxNP-8Kkwzi8Ko047p0BZBd3t6a0eIu4")


updater.dispatcher.add_handler(CommandHandler('start', start))
# updater.dispatcher.add_handler(MessageHandler(Filters.text('Inline'), inlinekeyboard))
updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))
# updater.dispatcher.add_handler(CallbackQueryHandler(callback_inline,pattern='like'))
# updater.dispatcher.add_handler(CallbackQueryHandler(callback_inline,pattern='dislike'))
updater.start_polling()
updater.idle()