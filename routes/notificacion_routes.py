from flask import Blueprint, request, jsonify, abort
from services.notificacion_service import (
    crear_notificacion,
    obtener_notificacion,
    obtener_todas_notificaciones,
    eliminar_notificacion
)

notificacion_bp = Blueprint('notificacion_bp', __name__)

@notificacion_bp.route('/notificaciones', methods=['POST'])
def create():
    data = request.get_json()
    try:
        nueva = crear_notificacion(data)
        return jsonify({'mensaje': 'Notificación creada exitosamente', 'id': nueva.id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@notificacion_bp.route('/notificaciones/<int:id>', methods=['GET'])
def get(id):
    notificacion = obtener_notificacion(id)
    if not notificacion:
        abort(404)
    return jsonify({
        'id': notificacion.id,
        'mensaje': notificacion.mensaje,
        'fecha': notificacion.fecha.isoformat(),
        'conductor_destino_id': notificacion.conductor_destino_id,
        'apoderado_destino_id': notificacion.apoderado_destino_id
    })

@notificacion_bp.route('/notificaciones', methods=['GET'])
def get_all():
    notificaciones = obtener_todas_notificaciones()
    return jsonify([{
        'id': n.id,
        'mensaje': n.mensaje,
        'fecha': n.fecha.isoformat(),
        'conductor_destino_id': n.conductor_destino_id,
        'apoderado_destino_id': n.apoderado_destino_id
    } for n in notificaciones])

@notificacion_bp.route('/notificaciones/<int:id>', methods=['DELETE'])
def delete(id):
    notificacion = obtener_notificacion(id)
    if not notificacion:
        abort(404)
    try:
        eliminar_notificacion(notificacion)
        return jsonify({'mensaje': 'Notificación eliminada exitosamente'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400
