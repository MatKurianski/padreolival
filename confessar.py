from enum import Enum
from telegram.ext import ConversationHandler, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from models import Pecado
import json

class FLUXO(Enum):
    ESCOLHER, RECOLHER_NOME, FIM = range(3)

def escolher_categoria(update, context):
    teclado_categorias = [[
        InlineKeyboardButton(text='Gula', callback_data='Gula'),
        InlineKeyboardButton(text='Ganância', callback_data='Ganância')
    ]]
    categorias_markup = InlineKeyboardMarkup(
        inline_keyboard=teclado_categorias
    )
    update.message.reply_text(
        'Que pena que pecaste, filho. Por favor, qual a categoria?\n',
        reply_markup=categorias_markup
    )
    return FLUXO.ESCOLHER

def escolher(update, context):
    _escolha = update.callback_query.data
    context.user_data['tipo'] = _escolha
    update.callback_query.edit_message_text('Insira o nome do seu pecado aqui')
    return FLUXO.RECOLHER_NOME

def recolher_nome(update, context):
    nome = update.message.text
    tipo = context.user_data['tipo']
    user = update.effective_user

    # TODO
    # if context.pecado['tipo'] == 'Ganância': return FLUXO.PERGUNTAR_PRECO

    pecado = Pecado(nome, tipo, user)
    result = pecado.save()
    update.message.reply_text(json.dumps(result, indent=2, default=str, ensure_ascii=False))
    return ConversationHandler.END

def cancel(update, context):
    return ConversationHandler.END

CONFESSAR = ConversationHandler(
    entry_points=[CommandHandler('confessar', escolher_categoria)],
    states={
        FLUXO.ESCOLHER: [CallbackQueryHandler(escolher)],
        FLUXO.RECOLHER_NOME: [MessageHandler(Filters.text, recolher_nome)]
    },
    fallbacks=[
        CommandHandler('cancel', cancel)
    ]
)
