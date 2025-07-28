from flask import Blueprint, jsonify, request, abort
from services.alumno_service import (
    obtener_todos_alumnos,
    obtener_alumno_por_id,
    crear_alumno,
    actualizar_alumno,
    eliminar_alumno
)

alumno_bp = Blueprint('alumno_bp', __name__)

@alumno_bp.route('/alumnos', methods=['GET'])
def get_all_alumnos():
    alumnos = obtener_todos_alumnos()
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

@alumno_bp.route('/alumnos/<int:id>', methods=['GET'])
def get_alumno(id):
    alumno = obtener_alumno_por_id(id)
    if not alumno:
        abort(404)
    return jsonify({
        'id': alumno.id,
        'nombre_completo': alumno.nombre_completo,
        'rut': alumno.rut,
        'fecha_nacimiento': alumno.fecha_nacimiento.isoformat(),
        'horario_entrada': alumno.horario_entrada.isoformat(),
        'horario_salida': alumno.horario_salida.isoformat(),
        'curso': alumno.curso,
        'direccion_hogar': alumno.direccion_hogar,
        'nombre_contacto_emergencia': alumno.nombre_contacto_emergencia,
        'contacto_emergencia': alumno.contacto_emergencia,
        'colegio_id': alumno.colegio_id,
        'apoderado_id': alumno.apoderado_id,
        'sector_id': alumno.sector_id
    })

@alumno_bp.route('/alumnos', methods=['POST'])
def crear_alumno_route():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Datos requeridos"}), 400

    try:
        nuevo = crear_alumno(data)
        return jsonify({
            "mensaje": "Alumno creado",
            "id": nuevo.id,
            "nombre": nuevo.nombre_completo,
            "rut": nuevo.rut
        }), 201
    except Exception as e:
        return jsonify({"error": f"Error al crear alumno: {str(e)}"}), 500


@alumno_bp.route('/alumnos/<int:id>', methods=['PUT'])
def update_alumno(id):
    alumno = obtener_alumno_por_id(id)
    if not alumno:
        abort(404)
    data = request.get_json()
    try:
        actualizar_alumno(alumno, data)
        return jsonify({'mensaje': 'Alumno actualizado exitosamente'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@alumno_bp.route('/alumnos/<int:id>', methods=['DELETE'])
def delete_alumno(id):
    alumno = obtener_alumno_por_id(id)
    if not alumno:
        abort(404)
    try:
        eliminar_alumno(alumno)
        return jsonify({'mensaje': 'Alumno eliminado exitosamente'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@alumno_bp.route('/api/alumno/registrar', methods=['POST'])
def registrar_alumno():
    data = request.get_json()
    try:
        nuevo = crear_alumno(data)
        return jsonify({'mensaje': 'Alumno registrado exitosamente', 'id': nuevo.id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

from services.alumno_service import obtener_alumnos_por_apoderado

@alumno_bp.route('/api/alumno/apoderado/<int:apoderado_id>', methods=['GET'])
def get_alumnos_por_apoderado(apoderado_id):
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

