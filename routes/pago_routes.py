from flask import Blueprint, request, jsonify, abort
from models import db, Pago

pago_bp = Blueprint('pago_bp', __name__)

@pago_bp.route('/pagos', methods=['POST'])
def create_pago():
    data = request.get_json()
    try:
        nuevo_pago = Pago(
            apoderado_id=data['apoderado_id'],
            contrato_id=data['contrato_id'],
            monto=data['monto'],
            completado=data['completado'],
            metodo_pago=data.get('metodo_pago')
        )
        db.session.add(nuevo_pago)
        db.session.commit()
        return jsonify({'mensaje': 'Pago creado exitosamente'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400


@pago_bp.route('/pagos/<int:id>', methods=['GET'])
def get_pago(id):
    pago = Pago.query.get(id)
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
def get_all_pagos():
    pagos = Pago.query.all()
    return jsonify([{
        'id': pago.id,
        'apoderado_id': pago.apoderado_id,
        'contrato_id': pago.contrato_id,
        'monto': pago.monto,
        'completado': pago.completado,
        'fecha_pago': pago.fecha_pago.isoformat(),
        'metodo_pago': pago.metodo_pago
    } for pago in pagos])


@pago_bp.route('/pagos/<int:id>', methods=['PUT'])
def update_pago(id):
    pago = Pago.query.get(id)
    if not pago:
        abort(404)
    data = request.get_json()
    try:
        pago.monto = data['monto']
        pago.completado = data['completado']
        pago.metodo_pago = data.get('metodo_pago')
        db.session.commit()
        return jsonify({'mensaje': 'Pago actualizado exitosamente'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400


@pago_bp.route('/pagos/<int:id>', methods=['DELETE'])
def delete_pago(id):
    pago = Pago.query.get(id)
    if not pago:
        abort(404)
    try:
        db.session.delete(pago)
        db.session.commit()
        return jsonify({'mensaje': 'Pago eliminado exitosamente'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400
