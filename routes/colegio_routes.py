from flask import Blueprint, jsonify, request, abort
from models import db, Colegio

colegio_bp = Blueprint('colegio_bp', __name__)

@colegio_bp.route('/colegios', methods=['POST'])
def create_colegio():
    data = request.get_json()
    try:
        nuevo_colegio = Colegio(
            rbd=data.get('rbd'),
            nombre_colegio=data.get('nombre_colegio'),
            direccion=data.get('direccion'),
            contacto=data.get('contacto'),
            sector_id=data['sector_id']
        )
        db.session.add(nuevo_colegio)
        db.session.commit()
        return jsonify({'mensaje': 'Colegio creado exitosamente'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400


@colegio_bp.route('/colegios/<int:id>', methods=['GET'])
def get_colegio(id):
    colegio = Colegio.query.get(id)
    if not colegio:
        abort(404)
    return jsonify({
        'id': colegio.id,
        'rbd': colegio.rbd,
        'nombre_colegio': colegio.nombre_colegio,
        'direccion': colegio.direccion,
        'contacto': colegio.contacto,
        'sector_id': colegio.sector_id
    })


@colegio_bp.route('/colegios', methods=['GET'])
def get_all_colegios():
    colegios = Colegio.query.all()
    return jsonify({'colegios': [{
        'id': colegio.id,
        'rbd': colegio.rbd,
        'nombre_colegio': colegio.nombre_colegio,
        'direccion': colegio.direccion,
        'contacto': colegio.contacto,
        'sector_id': colegio.sector_id
    } for colegio in colegios]})


@colegio_bp.route('/colegios/<int:id>', methods=['PUT'])
def update_colegio(id):
    colegio = Colegio.query.get(id)
    if not colegio:
        abort(404)
    data = request.get_json()
    try:
        colegio.rbd = data.get('rbd')
        colegio.nombre_colegio = data.get('nombre_colegio')
        colegio.direccion = data.get('direccion')
        colegio.contacto = data.get('contacto')
        colegio.sector_id = data['sector_id']
        db.session.commit()
        return jsonify({'mensaje': 'Colegio actualizado exitosamente'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400


@colegio_bp.route('/colegios/<int:id>', methods=['DELETE'])
def delete_colegio(id):
    colegio = Colegio.query.get(id)
    if not colegio:
        abort(404)
    try:
        db.session.delete(colegio)
        db.session.commit()
        return jsonify({'mensaje': 'Colegio eliminado exitosamente'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400
