# repositories/pago_repository.py

from models import db, Pago

def guardar(pago):
    db.session.add(pago)
    db.session.commit()
    return pago

def obtener_por_id(id):
    return Pago.query.get(id)

def obtener_todos():
    return Pago.query.all()

def actualizar():
    db.session.commit()

def eliminar(pago):
    db.session.delete(pago)
    db.session.commit()
