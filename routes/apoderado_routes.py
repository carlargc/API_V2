from flask import Blueprint, jsonify, request, abort
from flask import session
from services.alumno_service import obtener_alumnos_por_apoderado
from services.apoderado_service import (
    obtener_todos_apoderados,
    obtener_apoderado_por_id,
    crear_apoderado,
    actualizar_apoderado,
    eliminar_apoderado
)

apoderado_bp = Blueprint('apoderado_bp', __name__)

#crea apoderado
@apoderado_bp.route('/apoderados', methods=['POST'])
def crear_apoderado_route():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Datos requeridos"}), 400

    try:
        nuevo = crear_apoderado(data)
        return jsonify({
            "mensaje": "Apoderado creado",
            "id": nuevo.id,
            "nombre": nuevo.nombre_completo,
            "correo": nuevo.correo
        }), 201
    except Exception as e:
        return jsonify({"error": f"Error al crear apoderado: {str(e)}"}), 500


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

@apoderado_bp.route('/apoderado/registrar', methods=['POST'])
def registrar_apoderado_alias():
    data = request.get_json()
    try:
        nuevo = crear_apoderado(data)
        return jsonify({'mensaje': 'Apoderado registrado exitosamente', 'id': nuevo.id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400
@apoderado_bp.route('/apoderado/estudiantes', methods=['GET'])
def ver_estudiantes_apoderado():
    print("SESSION:", session) 
    if 'user_id' not in session or session.get('rol') != 'ROLE_APODERADO':
        abort(403)  # No autorizado

    apoderado_id = session['user_id']
    alumnos = obtener_alumnos_por_apoderado(apoderado_id)

    result = [{
        'id': a.id,
        'nombre_completo': a.nombre_completo,
        'rut': a.rut,
        'fecha_nacimiento': a.fecha_nacimiento.isoformat(),
        'horario_entrada': a.horario_entrada.isoformat(),
        'horario_salida': a.horario_salida.isoformat(),
        'curso': a.curso,
        'direccion_hogar': a.direccion_hogar,
        'nombre_contacto_emergencia': a.nombre_contacto_emergencia,
        'contacto_emergencia': a.contacto_emergencia,
        'colegio_id': a.colegio_id,
        'apoderado_id': a.apoderado_id,
        'sector_id': a.sector_id
    } for a in alumnos]

    return jsonify(result)