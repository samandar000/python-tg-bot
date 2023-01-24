import telegram
import os
import time
TOKEN = os.environ['TOKEN']

bot = telegram.Bot(token=TOKEN) 

def main():
    last_update_id = -1

    while True:
        curr_update = bot.getUpdates()[-1]
        curr_update_id = curr_update.update_id
        
        if curr_update_id != last_update_id:
            chat_id = curr_update.message.chat.id

            if curr_update.message.photo:
                photo = curr_update.message.photo[-1].file_id
                bot.sendPhoto(chat_id, photo)
            elif curr_update.message.sticker:
                bot.sendSticker(chat_id,curr_update.message.sticker)
                
            elif curr_update.message.text != '':
                bot.sendMessage(chat_id, curr_update.message.text)

            last_update_id = curr_update_id

        time.sleep(1)

main()
