from models import db, Solicitud

def guardar(solicitud):
    db.session.add(solicitud)
    db.session.commit()
    return solicitud

def obtener_por_id(id):
    return Solicitud.query.get(id)

def obtener_todos():
    return Solicitud.query.all()

def actualizar():
    db.session.commit()

def eliminar(solicitud):
    db.session.delete(solicitud)
    db.session.commit()
