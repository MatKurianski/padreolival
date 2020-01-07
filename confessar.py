from enum import Enum
from telegram.ext import ConversationHandler, CommandHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from gula import CONVERSA_GULA
from logger import LOGGER

class Categorias(Enum):
    ESCOLHER = "Escolher"
    GULA = "Gula"
    GANANCIA = "Ganancia"
    FIM = "Fim"

def escolher_categoria(update, context):
    teclado_categorias = [[
        InlineKeyboardButton(text='Gula', callback_data=Categorias.GULA.value),
        InlineKeyboardButton('Ganância', callback_data=Categorias.GANANCIA.value)
    ]]
    categorias_markup = InlineKeyboardMarkup(
        inline_keyboard=teclado_categorias
    )
    update.message.reply_text(
        'Que pena que pecaste, filho. Por favor, qual a categoria?\n',
        reply_markup=categorias_markup
    )
    return Categorias.ESCOLHER

def escolher(update, context):
    escolha = update.message.text
    usuario = update.effective_user.full_name
    if Categorias.GULA.value == escolha:
        LOGGER.info('{} escolheu "{}"'.format(usuario, escolha))
        return Categorias.GULA
    return ConversationHandler.END

def cancel(update, context):
    return ConversationHandler.END

CONFESSAR = ConversationHandler(
    entry_points=[CommandHandler('confessar', escolher_categoria)],
    states={
        Categorias.ESCOLHER: [CONVERSA_GULA]
    },
    fallbacks=[
        CommandHandler('cancel', cancel)
    ]
)
