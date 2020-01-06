from enum import Enum
from telegram.ext import ConversationHandler, CommandHandler, MessageHandler, Filters
from telegram import KeyboardButton, ReplyKeyboardMarkup

from logger import LOGGER

class Categorias(Enum):
    ESCOLHER = "Escolher"
    GULA = "Gula"
    GANANCIA = "Ganancia"
    FIM = "Fim"

def escolher_categoria(update, context):
    teclado_categorias = [[KeyboardButton('Gula'), KeyboardButton('Ganância')]]
    categorias_markup = ReplyKeyboardMarkup(
        keyboard=teclado_categorias,
        one_time_keyboard=True,
        resize_keyboard=True
    )
    update.message.reply_text(
        'Que pena que pecaste, filho. Por favor, qual a categoria?\n',
        reply_markup=categorias_markup
    )
    return Categorias.ESCOLHER

def escolher(update, context):
    escolha = update.message.text
    usuario = update.effective_user.full_name
    LOGGER.info('{} escolheu "{}"'.format(usuario, escolha))
    return ConversationHandler.END

def cancel(update, context):
    return ConversationHandler.END

CONFESSAR = ConversationHandler(
    entry_points=[CommandHandler('confessar', escolher_categoria)],
    states={
        Categorias.ESCOLHER: [MessageHandler(Filters.regex('^(Gula|Ganância)$'), escolher)]
    },
    fallbacks=[
        CommandHandler('cancel', cancel)
    ]
)