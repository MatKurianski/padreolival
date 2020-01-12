from enum import Enum
from telegram.ext import ConversationHandler, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from models import Pecado
import json

class FLUXO(Enum):
    ESCOLHER, RECOLHER_NOME, RECOLHER_PRECO, FIM = range(4)

def escolher_categoria(update, context):
    teclado_categorias = [[
        InlineKeyboardButton(text='Gula', callback_data='Gula'),
        InlineKeyboardButton(text='Ganância', callback_data='Ganância'),
        InlineKeyboardButton(text='Ambos', callback_data='Ambos')
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
    tipo = []

    if _escolha == "Ambos":
        tipo.append('Gula')
        tipo.append('Ganância')
    else:
        tipo.append(_escolha)
    context.user_data['tipo'] = tipo
    update.callback_query.edit_message_text('Qual foi seu pecado?')
    return FLUXO.RECOLHER_NOME

def recolher_nome(update, context):
    nome = update.message.text
    context.user_data['nome'] = nome

    tipo = context.user_data['tipo']

    if "Ganância" in tipo:
        update.message.reply_text('Quanto gastou?')
        return FLUXO.RECOLHER_PRECO
    return confirmar(update, context)

def recolher_preco(update, context):
    preco = float(update.message.text.replace(',', '.'))
    context.user_data['preço'] = preco
    return confirmar(update, context)

def confirmar(update, context):
    _pecado = context.user_data
    nome = 'Nome: ' + _pecado['nome']
    tipo = '\nTipo: ' + ','.join(_pecado['tipo'])
    preco = ''

    if 'preço' in _pecado.keys():
        preco = '\nPreço: R$ ' + str(_pecado['preço'])

    pecado_preview = nome + tipo + preco

    update.message.reply_text(
        'Deseja confirmar os dados do seu pecado?\n\n'+ pecado_preview,
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton(text='Concluir', callback_data='Concluir'),
            InlineKeyboardButton(text='Cancelar', callback_data='Cancelar')
        ]])
    )
    return FLUXO.FIM

def fim(update, context):
    res = update.callback_query.data
    if res == 'Concluir':
        pecado = Pecado(context.user_data, update.effective_user)
        result = pecado.save()
        update.callback_query.edit_message_text(
            'Concluído!\n\n'+
            json.dumps(result, indent=2, default=str, ensure_ascii=False)
        )
    else:
        update.callback_query.edit_message_text('Cancelado')
    return cancel(update, context)

def cancel(update, context):
    context.user_data.clear()
    return ConversationHandler.END

CONFESSAR = ConversationHandler(
    entry_points=[CommandHandler('confessar', escolher_categoria)],
    states={
        FLUXO.ESCOLHER: [CallbackQueryHandler(escolher)],
        FLUXO.RECOLHER_NOME: [MessageHandler(Filters.text, recolher_nome)],
        FLUXO.RECOLHER_PRECO: [MessageHandler(Filters.regex('^[0-9]+(\,[0-9]{1,2})?$'), recolher_preco)],
        FLUXO.FIM: [CallbackQueryHandler(fim)]
    },
    fallbacks=[
        CommandHandler('cancel', cancel)
    ]
)
