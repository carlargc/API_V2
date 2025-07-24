from flask import Blueprint, request, jsonify, abort
from services.pago_service import (
    crear_pago,
    obtener_pago_por_id,
    obtener_todos_pagos,
    actualizar_pago,
    eliminar_pago
)

pago_bp = Blueprint('pago_bp', __name__)

@pago_bp.route('/pagos', methods=['POST'])
def create_pago_route():
    data = request.get_json()
    try:
        nuevo = crear_pago(data)
        return jsonify({'mensaje': 'Pago creado exitosamente', 'id': nuevo.id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@pago_bp.route('/pagos/<int:id>', methods=['GET'])
def get_pago_route(id):
    pago = obtener_pago_por_id(id)
    if not pago:
        abort(404)
    return jsonify({
        'id': pago.id,
        'apoderado_id': pago.apoderado_id,
        'contrato_id': pago.contrato_id,
        'monto': pago.monto,
        'completado': pago.completado,
        'fecha_pago': pago.fecha_pago.isoformat(),
        'metodo_pago': pago.metodo_pago
    })

@pago_bp.route('/pagos', methods=['GET'])
def get_all_pagos_route():
    pagos = obtener_todos_pagos()
    return jsonify([{
        'id': p.id,
        'apoderado_id': p.apoderado_id,
        'contrato_id': p.contrato_id,
        'monto': p.monto,
        'completado': p.completado,
        'fecha_pago': p.fecha_pago.isoformat(),
        'metodo_pago': p.metodo_pago
    } for p in pagos])

@pago_bp.route('/pagos/<int:id>', methods=['PUT'])
def update_pago_route(id):
    pago = obtener_pago_por_id(id)
    if not pago:
        abort(404)
    data = request.get_json()
    try:
        actualizar_pago(pago, data)
        return jsonify({'mensaje': 'Pago actualizado exitosamente'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@pago_bp.route('/pagos/<int:id>', methods=['DELETE'])
def delete_pago_route(id):
    pago = obtener_pago_por_id(id)
    if not pago:
        abort(404)
    try:
        eliminar_pago(pago)
        return jsonify({'mensaje': 'Pago eliminado exitosamente'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400
