import os

from telegram.ext import Updater, CommandHandler
from dotenv import load_dotenv, find_dotenv

from confessar import CONFESSAR

load_dotenv(find_dotenv())

def start(update, context):
    update.message.reply_text('Salve!')

def main():
    telegram_toker = os.getenv("TELEGRAM_TOKEN")
    port = int(os.environ.get('PORT', '8443'))
    prod = os.environ.get('PROD', False)

    updater = Updater(token=telegram_toker, use_context=True)

    if prod:
        updater.start_webhook(listen="0.0.0.0", port=port, url_path=telegram_toker)
        updater.bot.set_webhook("https://padreolival.herokuapp.com/" + telegram_toker)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CONFESSAR)
    updater.start_polling()

    updater.idle()

if __name__ == "__main__":
    main()
