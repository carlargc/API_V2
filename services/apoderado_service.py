# services/apoderado_service.py
from models import Apoderado

from repositories.apoderado_repository import (
    guardar_apoderado,
    obtener_todos,
    obtener_por_id,
    eliminar,
    actualizar
)

def crear_apoderado(data):
    nuevo_apoderado = Apoderado(
        nombre_completo=data['nombre_completo'],
        rut=data['rut'],
        correo=data['correo'],
        password=data['password'],
        direccion=data['direccion'],
        numero_telefono=data['numero_telefono'],
        sexo=data.get('sexo'),
        rol=data.get('rol')
    )
    return guardar_apoderado(nuevo_apoderado)

def obtener_todos_apoderados():
    return obtener_todos()

def obtener_apoderado_por_id(id):
    return obtener_por_id(id)

def actualizar_apoderado(apoderado, data):
    apoderado.nombre_completo = data['nombre_completo']
    apoderado.rut = data['rut']
    apoderado.correo = data['correo']
    apoderado.password = data['password']
    apoderado.direccion = data['direccion']
    apoderado.numero_telefono = data['numero_telefono']
    apoderado.sexo = data.get('sexo')
    apoderado.rol = data.get('rol')
    actualizar()

def eliminar_apoderado(apoderado):
    eliminar(apoderado)
    
