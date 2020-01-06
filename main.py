from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import os

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update, context):
  update.message.reply_text('Salve!')

def main():
  TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
  PORT = int(os.environ.get('PORT', '8443'))
  PROD = os.environ.get('PROD', False)

  updater = Updater(token=TELEGRAM_TOKEN, use_context=True)

  if PROD:
    updater.start_webhook(listen="0.0.0.0",
                        port=PORT,
                        url_path=TELEGRAM_TOKEN)
    updater.bot.set_webhook("https://padreolival.herokuapp.com/" + TELEGRAM_TOKEN)

  dispatcher = updater.dispatcher

  dispatcher.add_handler(CommandHandler("start", start))
  updater.start_polling()

  updater.idle()

if __name__ == "__main__":
  main()