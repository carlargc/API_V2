# repositories/alumno_repository.py

from models import db, Alumno

def obtener_todos():
    return Alumno.query.all()

def obtener_por_id(id):
    return Alumno.query.get(id)

def guardar(alumno):
    db.session.add(alumno)
    db.session.commit()
    return alumno

def actualizar():
    db.session.commit()

def eliminar(alumno):
    db.session.delete(alumno)
    db.session.commit()
