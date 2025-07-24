from flask import Blueprint, request, jsonify, abort
from services.solicitud_service import (
    crear_solicitud,
    obtener_solicitud_por_id,
    obtener_todas_solicitudes,
    actualizar_solicitud,
    eliminar_solicitud
)

solicitud_bp = Blueprint('solicitud_bp', __name__)

@solicitud_bp.route('/solicitudes', methods=['POST'])
def create_solicitud_route():
    data = request.get_json()
    try:
        nueva = crear_solicitud(data)
        return jsonify({'mensaje': 'Solicitud creada exitosamente', 'id': nueva.id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@solicitud_bp.route('/solicitudes/<int:id>', methods=['GET'])
def get_solicitud_route(id):
    solicitud = obtener_solicitud_por_id(id)
    if not solicitud:
        abort(404)
    return jsonify({
        'id': solicitud.id,
        'apoderado_id': solicitud.apoderado_id,
        'conductor_id': solicitud.conductor_id,
        'furgon_id': solicitud.furgon_id,
        'aceptada': solicitud.aceptada,
        'rechazada': solicitud.rechazada,
        'vencida': solicitud.vencida,
        'estado': solicitud.estado
    })

@solicitud_bp.route('/solicitudes', methods=['GET'])
def get_all_solicitudes_route():
    solicitudes = obtener_todas_solicitudes()
    return jsonify([{
        'id': s.id,
        'apoderado_id': s.apoderado_id,
        'conductor_id': s.conductor_id,
        'furgon_id': s.furgon_id,
        'aceptada': s.aceptada,
        'rechazada': s.rechazada,
        'vencida': s.vencida,
        'estado': s.estado
    } for s in solicitudes])

@solicitud_bp.route('/solicitudes/<int:id>', methods=['PUT'])
def update_solicitud_route(id):
    solicitud = obtener_solicitud_por_id(id)
    if not solicitud:
        abort(404)
    data = request.get_json()
    try:
        actualizar_solicitud(solicitud, data)
        return jsonify({'mensaje': 'Solicitud actualizada exitosamente'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@solicitud_bp.route('/solicitudes/<int:id>', methods=['DELETE'])
def delete_solicitud_route(id):
    solicitud = obtener_solicitud_por_id(id)
    if not solicitud:
        abort(404)
    try:
        eliminar_solicitud(solicitud)
        return jsonify({'mensaje': 'Solicitud eliminada exitosamente'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400
