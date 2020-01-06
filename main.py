from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import os

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

def start(update, context):
  update.message.reply_text('Salve!')

def main():
  updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
  dispatcher = updater.dispatcher

  dispatcher.add_handler(CommandHandler("start", start))
  updater.start_polling()

  updater.idle()

if __name__ == "__main__":
  main()