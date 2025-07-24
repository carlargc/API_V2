# repositories/apoderado_repository.py
from models import db, Apoderado

def guardar_apoderado(apoderado):
    db.session.add(apoderado)
    db.session.commit()
    return apoderado

def obtener_todos():
    return Apoderado.query.all()

def obtener_por_id(id):
    return Apoderado.query.get(id)

def eliminar(apoderado):
    db.session.delete(apoderado)
    db.session.commit()

def actualizar():
    db.session.commit()
