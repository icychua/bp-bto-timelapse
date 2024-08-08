#!/usr/bin/python3

from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler
from telegram.constants import ParseMode

from picamera2 import Picamera2, Preview
from PIL import Image

import os
import nest_asyncio

def capture_photo():
    picam = Picamera2()

    config = picam.create_preview_configuration(main={"size":(1600,1200)})
    picam.configure(config)

    filename = "ad-hoc/temp.jpg"
    picam.start()
    picam.capture_file(filename)
    picam.close()
    
    return filename

nest_asyncio.apply()
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    """Send a message when the command /start is issued."""
    #Get info of user
    user = update.effective_user
    userid_value = str(user.id)
    
    welcome_message = """
For authorised users only.
"""
    print(user.id)
    await update.message.reply_html(welcome_message)

async def snap(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    """Send a message when the command /start is issued."""
    #Get info of user
    user = update.effective_user
    userid_value = str(user.id)
    if userid_value in ["1115768283","1079104485"]:
        message = "You are authorised"
        photo = capture_photo()
        await update.message.reply_photo(photo)
    else:
        message = """
    are you trying to hack
    """
        print(user.id)
        await update.message.reply_html(message)

AVAILABLE_COMMANDS = ["/start", "/snap"]

def main() -> None:
    application = Application.builder().token(os.environ['BP_TEL_TOKEN']).concurrent_updates(True).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("snap", snap))
    
    #Run until bot is stopped
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()

