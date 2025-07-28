from datetime import datetime
from models import Documentos
 # o desde donde lo tengas definido

from repositories.documento_repository import (
    guardar_documento,
    obtener_documento_por_id,
    obtener_todos,
    eliminar_documento as eliminar_repo
)

def crear_documento(data):
    documento = Documentos(
        contenido_documento=data['contenido_documento'].encode('utf-8'),
        tipo_documento=data['tipo_documento'],
        conductor_id=data.get('conductor_id'),
        asistente_id=data.get('asistente_id')
    )
    return guardar_documento(documento)

def obtener_documento(id):
    return obtener_documento_por_id(id)

def obtener_todos_documentos():
    return obtener_todos()

def actualizar_documento(documento, data):
    documento.tipo_documento = data['tipo_documento']
    documento.contenido_documento = data['contenido_documento'].encode('utf-8')
    guardar_documento(documento)

def eliminar_documento(documento):
    eliminar_repo(documento)

def obtener_documentos_por_conductor(conductor_id):
    return Documentos.query.filter_by(conductor_id=conductor_id).all()