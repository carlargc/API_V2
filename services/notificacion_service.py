from models import db, Notificacion
from repositories.notificacion_repository import (
    guardar,
    obtener_por_id,
    obtener_todos,
    eliminar
)

def crear_notificacion(data):
    nueva = Notificacion(
        mensaje=data['mensaje'],
        conductor_destino_id=data.get('conductor_destino_id'),
        apoderado_destino_id=data.get('apoderado_destino_id')
    )
    return guardar(nueva)

def obtener_notificacion(id):
    return obtener_por_id(id)

def obtener_todas_notificaciones():
    return obtener_todos()

def eliminar_notificacion(notificacion):
    eliminar(notificacion)

