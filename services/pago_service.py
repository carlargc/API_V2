# services/pago_service.py

from models import Pago
from repositories.pago_repository import (
    guardar,
    obtener_por_id,
    obtener_todos,
    actualizar,
    eliminar
)

def crear_pago(data):
    nuevo_pago = Pago(
        apoderado_id=data['apoderado_id'],
        contrato_id=data['contrato_id'],
        monto=data['monto'],
        completado=data['completado'],
        metodo_pago=data.get('metodo_pago')
    )
    return guardar(nuevo_pago)

def obtener_pago_por_id(id):
    return obtener_por_id(id)

def obtener_todos_pagos():
    return obtener_todos()

def actualizar_pago(pago, data):
    pago.monto = data['monto']
    pago.completado = data['completado']
    pago.metodo_pago = data.get('metodo_pago')
    actualizar()
    return pago

def eliminar_pago(pago):
    eliminar(pago)
