from flask import Blueprint, jsonify, request, abort
from services.colegio_service import (
    crear_colegio,
    obtener_colegio_por_id,
    obtener_todos_los_colegios,
    actualizar_colegio,
    eliminar_colegio
)

colegio_bp = Blueprint('colegio_bp', __name__)

@colegio_bp.route('/colegios', methods=['POST'])
def create_colegio():
    data = request.get_json()
    try:
        nuevo = crear_colegio(data)
        return jsonify({'mensaje': 'Colegio creado exitosamente', 'id': nuevo.id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@colegio_bp.route('/colegios/<int:id>', methods=['GET'])
def get_colegio(id):
    colegio = obtener_colegio_por_id(id)
    if not colegio:
        abort(404)
    return jsonify(colegio)

@colegio_bp.route('/colegios', methods=['GET'])
def get_all_colegios():
    return jsonify({'colegios': obtener_todos_los_colegios()})

@colegio_bp.route('/colegios/<int:id>', methods=['PUT'])
def update_colegio(id):
    data = request.get_json()
    try:
        actualizado = actualizar_colegio(id, data)
        if not actualizado:
            abort(404)
        return jsonify({'mensaje': 'Colegio actualizado exitosamente'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@colegio_bp.route('/colegios/<int:id>', methods=['DELETE'])
def delete_colegio(id):
    try:
        eliminado = eliminar_colegio(id)
        if not eliminado:
            abort(404)
        return jsonify({'mensaje': 'Colegio eliminado exitosamente'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400
