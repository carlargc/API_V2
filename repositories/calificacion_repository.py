from models import db, Calificacion

def guardar_calificacion(calificacion):
    db.session.add(calificacion)
    db.session.commit()
    return calificacion

def obtener_calificacion_por_id(id):
    return Calificacion.query.get(id)

def obtener_todas_calificaciones():
    return Calificacion.query.all()

def actualizar_calificacion_en_db():
    db.session.commit()

def eliminar_calificacion(calificacion):
    db.session.delete(calificacion)
    db.session.commit()
