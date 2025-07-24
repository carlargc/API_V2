from flask import Blueprint, jsonify, request, abort
from services.apoderado_service import (
    obtener_todos_apoderados,
    obtener_apoderado_por_id,
    crear_apoderado,
    actualizar_apoderado,
    eliminar_apoderado
)

apoderado_bp = Blueprint('apoderado_bp', __name__)

# Crear apoderado
@apoderado_bp.route('/apoderados', methods=['POST'])
def create_apoderado():
    data = request.get_json()
    try:
        nuevo = crear_apoderado(data)
        return jsonify({'mensaje': 'Apoderado creado exitosamente', 'id': nuevo.id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Obtener todos
@apoderado_bp.route('/apoderados', methods=['GET'])
def get_all_apoderados():
    apoderados = obtener_todos_apoderados()
    result = []
    for apoderado in apoderados:
        result.append({
            'id': apoderado.id,
            'nombre_completo': apoderado.nombre_completo,
            'rut': apoderado.rut,
            'correo': apoderado.correo,
            'direccion': apoderado.direccion,
            'numero_telefono': apoderado.numero_telefono,
            'sexo': apoderado.sexo,
            'rol': apoderado.rol
        })
    return jsonify(result)

# Obtener uno
@apoderado_bp.route('/apoderados/<int:id>', methods=['GET'])
def get_apoderado(id):
    apoderado = obtener_apoderado_por_id(id)
    if not apoderado:
        abort(404)
    return jsonify({
        'id': apoderado.id,
        'nombre_completo': apoderado.nombre_completo,
        'rut': apoderado.rut,
        'correo': apoderado.correo,
        'direccion': apoderado.direccion,
        'numero_telefono': apoderado.numero_telefono,
        'sexo': apoderado.sexo,
        'rol': apoderado.rol
    })

# Actualizar
@apoderado_bp.route('/apoderados/<int:id>', methods=['PUT'])
def update_apoderado(id):
    apoderado = obtener_apoderado_por_id(id)
    if not apoderado:
        abort(404)
    data = request.get_json()
    try:
        actualizar_apoderado(apoderado, data)
        return jsonify({'mensaje': 'Apoderado actualizado exitosamente'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Eliminar
@apoderado_bp.route('/apoderados/<int:id>', methods=['DELETE'])
def delete_apoderado(id):
    apoderado = obtener_apoderado_por_id(id)
    if not apoderado:
        abort(404)
    try:
        eliminar_apoderado(apoderado)
        return jsonify({'mensaje': 'Apoderado eliminado exitosamente'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400
