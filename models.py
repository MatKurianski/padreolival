from datetime import datetime
from db import db

class Pecado:
    def __init__(self, nome, user):
        self.nome = nome
        self.user = {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username,
        }

    def save(self):
        pass

class PecadoGula(Pecado):
    def save(self):
        _novo_pecado = {
            'nome': self.nome,
            'user': self.user,
            'tipo': 'Gula',
            'data': datetime.utcnow()
        }
        novo_pecado = _novo_pecado.copy()
        db.pecado.insert_one(novo_pecado)
        return _novo_pecado
