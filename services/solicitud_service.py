from models import Solicitud
from repositories.solicitud_repository import (
    guardar,
    obtener_por_id,
    obtener_todos,
    actualizar,
    eliminar
)

def crear_solicitud(data):
    nueva = Solicitud(
        apoderado_id=data['apoderado_id'],
        conductor_id=data['conductor_id'],
        furgon_id=data['furgon_id'],
        aceptada=data.get('aceptada', False),
        rechazada=data.get('rechazada', False),
        vencida=data.get('vencida', False),
        estado=data.get('estado')
    )
    return guardar(nueva)

def obtener_solicitud_por_id(id):
    return obtener_por_id(id)

def obtener_todas_solicitudes():
    return obtener_todos()

def actualizar_solicitud(solicitud, data):
    solicitud.aceptada = data.get('aceptada', solicitud.aceptada)
    solicitud.rechazada = data.get('rechazada', solicitud.rechazada)
    solicitud.vencida = data.get('vencida', solicitud.vencida)
    solicitud.estado = data.get('estado', solicitud.estado)
    actualizar()
    return solicitud

def eliminar_solicitud(solicitud):
    eliminar(solicitud)
