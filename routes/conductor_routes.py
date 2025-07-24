from flask import Blueprint, request, jsonify
from services.conductor_service import (
    crear_conductor,
    obtener_conductores,
    obtener_conductor_por_id,
    actualizar_conductor,
    eliminar_conductor
)

conductor_bp = Blueprint('conductor_bp', __name__)

@conductor_bp.route('/conductores', methods=['POST'])
def create_conductor():
    data = request.get_json()
    try:
        nuevo = crear_conductor(data)
        return jsonify({"message": "Conductor creado exitosamente", "id": nuevo.id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@conductor_bp.route('/conductores', methods=['GET'])
def get_conductores():
    return jsonify({"conductores": obtener_conductores()})

@conductor_bp.route('/conductores/<int:id>', methods=['GET'])
def get_conductor(id):
    conductor = obtener_conductor_por_id(id)
    if not conductor:
        return jsonify({"error": "Conductor no encontrado"}), 404
    return jsonify(conductor)

@conductor_bp.route('/conductores/<int:id>', methods=['PUT'])
def update_conductor(id):
    data = request.get_json()
    try:
        actualizado = actualizar_conductor(id, data)
        if not actualizado:
            return jsonify({"error": "Conductor no encontrado"}), 404
        return jsonify({"message": "Conductor actualizado exitosamente"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@conductor_bp.route('/conductores/<int:id>', methods=['DELETE'])
def delete_conductor(id):
    eliminado = eliminar_conductor(id)
    if not eliminado:
        return jsonify({"error": "Conductor no encontrado"}), 404
    return jsonify({"message": "Conductor eliminado exitosamente"})
