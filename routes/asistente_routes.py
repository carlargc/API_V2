from flask import Blueprint, jsonify, request, abort
from services.asistente_service import (
    obtener_asistente_por_id,
    obtener_todos_asistentes,
    crear_asistente,
    actualizar_asistente,
    eliminar_asistente
)

asistente_bp = Blueprint('asistente_bp', __name__)

@asistente_bp.route('/asistentes/<int:id>', methods=['GET'])
def get_asistente(id):
    asistente = obtener_asistente_por_id(id)
    if not asistente:
        abort(404)
    return jsonify(asistente)

@asistente_bp.route('/asistentes', methods=['GET'])
def get_all_asistentes():
    asistentes = obtener_todos_asistentes()
    return jsonify(asistentes)

@asistente_bp.route('/asistentes', methods=['POST'])
def create_asistente_route():
    data = request.get_json()
    try:
        nuevo = crear_asistente(data)
        return jsonify({'mensaje': 'Asistente creado exitosamente', 'id': nuevo.id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@asistente_bp.route('/asistentes/<int:id>', methods=['PUT'])
def update_asistente(id):
    data = request.get_json()
    try:
        actualizado = actualizar_asistente(id, data)
        if not actualizado:
            abort(404)
        return jsonify({'mensaje': 'Asistente actualizado exitosamente'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@asistente_bp.route('/asistentes/<int:id>', methods=['DELETE'])
def delete_asistente(id):
    try:
        eliminado = eliminar_asistente(id)
        if not eliminado:
            abort(404)
        return jsonify({'mensaje': 'Asistente eliminado exitosamente'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

