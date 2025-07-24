from repositories import calificacion_repository as repo
from models import Calificacion

def calificacion_a_dict(cal):
    return {
        'id': cal.id,
        'apoderado_id': cal.apoderado_id,
        'conductor_id': cal.conductor_id,
        'contrato_id': cal.contrato_id,
        'puntuacion': cal.puntuacion,
        'comentario': cal.comentario,
        'fecha_calificacion': cal.fecha_calificacion.isoformat()
    }

def crear_calificacion(data):
    nueva = Calificacion(
        apoderado_id=data['apoderado_id'],
        conductor_id=data['conductor_id'],
        contrato_id=data['contrato_id'],
        puntuacion=data['puntuacion'],
        comentario=data.get('comentario')
    )
    return repo.guardar_calificacion(nueva)

def obtener_calificacion_por_id(id):
    cal = repo.obtener_calificacion_por_id(id)
    return calificacion_a_dict(cal) if cal else None

def obtener_todas_calificaciones():
    calificaciones = repo.obtener_todas_calificaciones()
    return [calificacion_a_dict(c) for c in calificaciones]

def actualizar_calificacion(id, data):
    cal = repo.obtener_calificacion_por_id(id)
    if not cal:
        return None
    cal.puntuacion = data['puntuacion']
    cal.comentario = data.get('comentario')
    repo.actualizar_calificacion_en_db()
    return cal

def eliminar_calificacion(id):
    cal = repo.obtener_calificacion_por_id(id)
    if not cal:
        return None
    repo.eliminar_calificacion(cal)
    return cal

