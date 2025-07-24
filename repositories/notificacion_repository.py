# repositories/notificacion_repository.py

from models import db, Notificacion

def guardar(notificacion):
    db.session.add(notificacion)
    db.session.commit()
    return notificacion

def obtener_por_id(id):
    return Notificacion.query.get(id)

def obtener_todos():
    return Notificacion.query.all()

def eliminar(notificacion):
    db.session.delete(notificacion)
    db.session.commit()
