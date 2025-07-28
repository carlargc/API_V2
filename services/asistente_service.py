import base64
from repositories.asistente_repository import (
    get_asistente_by_id,
    get_all_asistentes,
    save_asistente,
    update_asistente,
    delete_asistente
)
from models import Asistente

def asistente_a_dict(asistente):
    return {
        'id': asistente.id,
        'correo': asistente.correo,
        'nombre_completo': asistente.nombre_completo,
        'rut': asistente.rut,
        'sexo': asistente.sexo,
        'telefono': asistente.telefono,
        'image': base64.b64encode(asistente.image).decode('utf-8') if asistente.image else None,
        'conductor_id': asistente.conductor_id,
        'furgon_id': asistente.furgon_id
    }

def obtener_asistente_por_id(id):
    return Asistente.query.get(id)

def obtener_todos_asistentes():
    asistentes = get_all_asistentes()
    return [asistente_a_dict(a) for a in asistentes]

def crear_asistente(data):
    nuevo_asistente = Asistente(
        correo=data['correo'],
        nombre_completo=data['nombre_completo'],
        rut=data['rut'],
        sexo=data.get('sexo'),
        telefono=data['telefono'],
        image=base64.b64decode(data['image']) if data.get('image') else None,
        conductor_id=data['conductor_id'],
        furgon_id=data.get('furgon_id')
    )
    return save_asistente(nuevo_asistente)

def actualizar_asistente(id, data):
    asistente = get_asistente_by_id(id)
    if not asistente:
        return None
    asistente.correo = data['correo']
    asistente.nombre_completo = data['nombre_completo']
    asistente.rut = data['rut']
    asistente.sexo = data.get('sexo')
    asistente.telefono = data['telefono']
    if data.get('image'):
        asistente.image = base64.b64decode(data['image'])
    asistente.conductor_id = data['conductor_id']
    asistente.furgon_id = data.get('furgon_id')
    update_asistente()
    return asistente

def eliminar_asistente(id):
    asistente = get_asistente_by_id(id)
    if not asistente:
        return None
    delete_asistente(asistente)
    return asistente
