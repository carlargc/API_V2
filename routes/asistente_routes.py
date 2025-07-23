from flask import Blueprint, jsonify, request, abort
from models import db, Asistente
import base64

asistente_bp = Blueprint('asistente_bp', __name__)


@asistente_bp.route('/asistentes/<int:id>', methods=['GET'])
def get_asistente(id):
    asistente = Asistente.query.get(id)
    if not asistente:
        abort(404)
    return jsonify({
        'id': asistente.id,
        'correo': asistente.correo,
        'nombre_completo': asistente.nombre_completo,
        'rut': asistente.rut,
        'sexo': asistente.sexo,
        'telefono': asistente.telefono,
        'image': base64.b64encode(asistente.image).decode('utf-8') if asistente.image else None,
        'conductor_id': asistente.conductor_id,
        'furgon_id': asistente.furgon_id
    })


@asistente_bp.route('/asistentes', methods=['GET'])
def get_all_asistentes():
    asistentes = Asistente.query.all()
    result = []
    for asistente in asistentes:
        result.append({
            'id': asistente.id,
            'correo': asistente.correo,
            'nombre_completo': asistente.nombre_completo,
            'rut': asistente.rut,
            'sexo': asistente.sexo,
            'telefono': asistente.telefono,
            'image': base64.b64encode(asistente.image).decode('utf-8') if asistente.image else None,
            'conductor_id': asistente.conductor_id,
            'furgon_id': asistente.furgon_id
        })
    return jsonify(result)


@asistente_bp.route('/asistentes/<int:id>', methods=['PUT'])
def update_asistente(id):
    asistente = Asistente.query.get(id)
    if not asistente:
        abort(404)
    data = request.get_json()
    try:
        asistente.correo = data['correo']
        asistente.nombre_completo = data['nombre_completo']
        asistente.rut = data['rut']
        asistente.sexo = data.get('sexo')
        asistente.telefono = data['telefono']
        if data.get('image'):
            asistente.image = base64.b64decode(data['image'])
        asistente.conductor_id = data['conductor_id']
        asistente.furgon_id = data.get('furgon_id')
        db.session.commit()
        return jsonify({'mensaje': 'Asistente actualizado exitosamente'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400


@asistente_bp.route('/asistentes/<int:id>', methods=['DELETE'])
def delete_asistente(id):
    asistente = Asistente.query.get(id)
    if not asistente:
        abort(404)
    try:
        db.session.delete(asistente)
        db.session.commit()
        return jsonify({'mensaje': 'Asistente eliminado exitosamente'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400


import base64

@asistente_bp.route('/asistentes', methods=['POST'])
def create_asistente():
    data = request.get_json()
    try:
        nuevo_asistente = Asistente(
            correo=data['correo'],
            nombre_completo=data['nombre_completo'],
            rut=data['rut'],
            sexo=data.get('sexo'),
            telefono=data['telefono'],
            image=base64.b64decode(data['image']) if data.get('image') else None,
            conductor_id=data['conductor_id'],
            furgon_id=data.get('furgon_id')
        )
        db.session.add(nuevo_asistente)
        db.session.commit()
        return jsonify({'mensaje': 'Asistente creado exitosamente'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400
