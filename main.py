import telegram
import os
import time
TOKEN = os.environ['TOKEN']

bot = telegram.Bot(token=TOKEN)

def main():
    last_update = bot.getUpdates()[-1]
    last_update_id = last_update.update_id

    while True:
        curr_update = bot.getUpdates()[-1]
        curr_update_id = curr_update.update_id
        
        if curr_update_id != last_update_id:
            chat_id = curr_update.message.chat.id
            if curr_update.message.text != None:
                text = curr_update.message.text
                bot.sendMessage(chat_id,text)
            elif curr_update.message.photo != []:
                photo = curr_update.message.photo[-1].file_id
                bot.sendPhoto(chat_id, photo)
        
            # elif curr_update.message.text != '':
            #     bot.sendMessage(chat_id, curr_update.message.text)
            
            elif curr_update.message.video != []:
                video = curr_update.message.video.file_id
                bot.sendSticker(chat_id,video)
            elif curr_update.message.sticker != []:
                sticker = curr_update.message.sticker.file_id
                bot.sendSticker(chat_id,sticker)

            last_update_id = curr_update_id

        time.sleep(1)

main()