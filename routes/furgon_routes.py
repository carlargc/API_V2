from flask import Blueprint, request, jsonify, abort
from services.furgon_service import (
    crear_furgon,
    obtener_furgon,
    obtener_todos_furgones,
    actualizar_furgon,
    eliminar_furgon,
    filtrar_furgones
)

furgon_bp = Blueprint('furgon_bp', __name__)

@furgon_bp.route('/furgones', methods=['POST'])
def create():
    data = request.get_json()
    try:
        nuevo = crear_furgon(data)
        return jsonify({'mensaje': 'Furgón creado exitosamente', 'id': nuevo.id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@furgon_bp.route('/furgones/<int:id>', methods=['GET'])
def get(id):
    furgon = obtener_furgon(id)
    if not furgon:
        abort(404)
    return jsonify({
        'id': furgon.id,
        'patente': furgon.patente,
        'marca': furgon.marca,
        'modelo': furgon.modelo,
        'ano': furgon.ano,
        'capacidad': furgon.capacidad,
        'cupos_disponibles': furgon.cupos_disponibles,
        'precio_base': furgon.precio_base,
        'validado': furgon.validado,
        'conductor_id': furgon.conductor_id,
        'sector_id': furgon.sector_id,
        'colegio_id': furgon.colegio_id
    })

@furgon_bp.route('/furgones', methods=['GET'])
def get_all():
    comuna = request.args.get('comuna')
    colegio_id = request.args.get('colegio')
    poblacion = request.args.get('poblacion')

    if comuna or colegio_id or poblacion:
        furgones = filtrar_furgones(comuna, colegio_id, poblacion)
    else:
        furgones = obtener_todos_furgones()

    result = [{
        'id': f.id,
        'patente': f.patente,
        'marca': f.marca,
        'modelo': f.modelo,
        'ano': f.ano,
        'capacidad': f.capacidad,
        'cupos_disponibles': f.cupos_disponibles,
        'precio_base': f.precio_base,
        'validado': f.validado,
        'sector_id': f.sector_id,
        'colegio_id': f.colegio_id,
        'conductor_id': f.conductor_id
    } for f in furgones]
    return jsonify(result)

@furgon_bp.route('/furgones/<int:id>', methods=['PUT'])
def update(id):
    furgon = obtener_furgon(id)
    if not furgon:
        abort(404)
    data = request.get_json()
    try:
        actualizar_furgon(furgon, data)
        return jsonify({'mensaje': 'Furgón actualizado exitosamente'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@furgon_bp.route('/furgones/<int:id>', methods=['DELETE'])
def delete(id):
    furgon = obtener_furgon(id)
    if not furgon:
        abort(404)
    try:
        eliminar_furgon(furgon)
        return jsonify({'mensaje': 'Furgón eliminado exitosamente'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400
