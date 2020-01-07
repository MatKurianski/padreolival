from enum import Enum

from telegram.ext import ConversationHandler, MessageHandler, Filters, CallbackQueryHandler

class FasesGula(Enum):
    NOME = 'Nome'
    FIM = 'Fim'

def _nome_gula(update, context):
    update.callback_query.edit_message_text("Vejo que caiu na tentação da gula...")
    update.callback_query.message.reply_text('O que você comeu de porcaria?')
    return FasesGula.FIM

def _fim_gula(update, context):
    res = update.message.text
    update.message.reply_text("Vejo que respondeu \"{}\"".format(res))
    return ConversationHandler.END

CONVERSA_GULA = ConversationHandler(
    entry_points=[CallbackQueryHandler(_nome_gula, pattern='^Gula$')],
    states={
        FasesGula.FIM: [MessageHandler(Filters.text, _fim_gula)]
    },
    fallbacks=[]
)
