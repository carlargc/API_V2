from flask import Blueprint, request, jsonify, abort
from services.calificacion_service import (
    crear_calificacion,
    obtener_calificacion_por_id,
    obtener_todas_calificaciones,
    actualizar_calificacion,
    eliminar_calificacion
)

calificacion_bp = Blueprint('calificacion_bp', __name__)

@calificacion_bp.route('/calificaciones', methods=['POST'])
def create_calificacion():
    data = request.get_json()
    try:
        nueva = crear_calificacion(data)
        return jsonify({'mensaje': 'Calificación creada exitosamente', 'id': nueva.id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@calificacion_bp.route('/calificaciones/<int:id>', methods=['GET'])
def get_calificacion(id):
    calificacion = obtener_calificacion_por_id(id)
    if not calificacion:
        abort(404)
    return jsonify(calificacion)

@calificacion_bp.route('/calificaciones', methods=['GET'])
def get_all_calificaciones():
    return jsonify(obtener_todas_calificaciones())

@calificacion_bp.route('/calificaciones/<int:id>', methods=['PUT'])
def update_calificacion(id):
    data = request.get_json()
    try:
        actualizado = actualizar_calificacion(id, data)
        if not actualizado:
            abort(404)
        return jsonify({'mensaje': 'Calificación actualizada exitosamente'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@calificacion_bp.route('/calificaciones/<int:id>', methods=['DELETE'])
def delete_calificacion(id):
    try:
        eliminado = eliminar_calificacion(id)
        if not eliminado:
            abort(404)
        return jsonify({'mensaje': 'Calificación eliminada exitosamente'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400
