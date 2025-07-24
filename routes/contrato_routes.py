from flask import Blueprint, request, jsonify, abort
from services.contrato_service import (
    crear_contrato,
    obtener_contrato,
    obtener_todos_contratos,
    actualizar_contrato,
    eliminar_contrato
)

contrato_bp = Blueprint('contrato_bp', __name__)

@contrato_bp.route('/contrato', methods=['POST'])
def create_contrato_route():
    data = request.get_json()
    try:
        nuevo = crear_contrato(data)
        return jsonify({'mensaje': 'Contrato creado exitosamente', 'id': nuevo.id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@contrato_bp.route('/contrato/<int:id>', methods=['GET'])
def get_contrato_route(id):
    contrato = obtener_contrato(id)
    if not contrato:
        abort(404)
    return jsonify({
        'id': contrato.id,
        'direccion_establecimiento': contrato.direccion_establecimiento,
        'direccion_hogar': contrato.direccion_hogar,
        'fecha_contratacion': contrato.fecha_contratacion.isoformat(),
        'nombre_alumno': contrato.nombre_alumno,
        'nombre_apoderado': contrato.nombre_apoderado,
        'rut_apoderado': contrato.rut_apoderado,
        'nombre_establecimiento': contrato.nombre_establecimiento,
        'periodo': contrato.periodo,
        'precio': contrato.precio,
        'estado': contrato.estado,
        'tipo_servicio': contrato.tipo_servicio,
        'nombre_contacto_emergencia': contrato.nombre_contacto_emergencia,
        'numero_contacto_emergencia': contrato.numero_contacto_emergencia,
        'furgon_id': contrato.furgon_id,
        'conductor_id': contrato.conductor_id,
        'apoderado_id': contrato.apoderado_id,
        'alumno_id': contrato.alumno_id,
        'colegio_id': contrato.colegio_id
    })

@contrato_bp.route('/contrato', methods=['GET'])
def get_all_contratos_route():
    contratos = obtener_todos_contratos()
    result = [{
        'id': c.id,
        'direccion_establecimiento': c.direccion_establecimiento,
        'direccion_hogar': c.direccion_hogar,
        'fecha_contratacion': c.fecha_contratacion.isoformat(),
        'nombre_alumno': c.nombre_alumno,
        'nombre_apoderado': c.nombre_apoderado,
        'rut_apoderado': c.rut_apoderado,
        'nombre_establecimiento': c.nombre_establecimiento,
        'periodo': c.periodo,
        'precio': c.precio,
        'estado': c.estado,
        'tipo_servicio': c.tipo_servicio,
        'nombre_contacto_emergencia': c.nombre_contacto_emergencia,
        'numero_contacto_emergencia': c.numero_contacto_emergencia,
        'furgon_id': c.furgon_id,
        'conductor_id': c.conductor_id,
        'apoderado_id': c.apoderado_id,
        'alumno_id': c.alumno_id,
        'colegio_id': c.colegio_id
    } for c in contratos]
    return jsonify(result)

@contrato_bp.route('/contrato/<int:id>', methods=['PUT'])
def update_contrato_route(id):
    contrato = obtener_contrato(id)
    if not contrato:
        abort(404)
    data = request.get_json()
    try:
        actualizar_contrato(contrato, data)
        return jsonify({'mensaje': 'Contrato actualizado exitosamente'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@contrato_bp.route('/contrato/<int:id>', methods=['DELETE'])
def delete_contrato_route(id):
    contrato = obtener_contrato(id)
    if not contrato:
        abort(404)
    try:
        eliminar_contrato(contrato)
        return jsonify({'mensaje': 'Contrato eliminado exitosamente'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400
