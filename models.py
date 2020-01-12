import os
from datetime import datetime
from db import db

PROD = os.environ.get('PROD', False)

if PROD:
    pecados = db.pecado
else:
    pecados = db.development

class Pecado:
    def __init__(self, pecado, user):
        pecado['data'] = datetime.utcnow()
        _user = {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username,
        }
        pecado['user'] = _user
        self.pecado = pecado

    def save(self):
        novo_pecado = self.pecado.copy()
        return novo_pecado
