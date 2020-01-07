from enum import Enum
import json

from telegram.ext import ConversationHandler, MessageHandler, Filters, CallbackQueryHandler, CommandHandler
from models import PecadoGula

class FasesGula(Enum):
    NOME = 'Nome'
    FIM = 'Fim'

def _nome_gula(update, context):
    update.callback_query.edit_message_text("Vejo que caiu na tentação da gula...")
    update.callback_query.message.reply_text('O que você comeu de porcaria?')
    return FasesGula.FIM

def _fim_gula(update, context):
    nome_pecado = update.message.text
    usuario = update.effective_user
    novo_pecado = PecadoGula(nome_pecado, usuario)
    result = novo_pecado.save()
    update.message.reply_text(json.dumps(result, indent=2, default=str, ensure_ascii=False))
    return ConversationHandler.END

CONVERSA_GULA = ConversationHandler(
    entry_points=[CallbackQueryHandler(_nome_gula, pattern='^Gula$')],
    states={
        FasesGula.FIM: [MessageHandler(Filters.text, _fim_gula)]
    },
    fallbacks=[
        CommandHandler('cancel', lambda update, context: ConversationHandler.END)
    ],
    map_to_parent={
        ConversationHandler.END: ConversationHandler.END
    }
)
