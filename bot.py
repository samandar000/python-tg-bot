import telegram
import os
import time


TOKEN = os.environ['TOKEN']

bot = telegram.Bot(token=TOKEN)

last_update = bot.getUpdates()[-1]

last_update_id = last_update.update_id

curr_update = bot.getUpdates()[-1]
        
curr_update_id = last_update.update_id

stiker = curr_update.message.text
# photo = last_update.message.sticker.file_id


print(stiker)