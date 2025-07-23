from flask import Blueprint, jsonify, request, abort
from models import db, Apoderado

apoderado_bp = Blueprint('apoderado_bp', __name__)

# Crear un nuevo apoderado
@apoderado_bp.route('/apoderados', methods=['POST'])
def create_apoderado():
    data = request.get_json()
    try:
        nuevo_apoderado = Apoderado(
            nombre_completo=data['nombre_completo'],
            rut=data['rut'],
            correo=data['correo'],
            password=data['password'],  # Ideal cifrarla en producción
            direccion=data['direccion'],
            numero_telefono=data['numero_telefono'],
            sexo=data.get('sexo'),
            rol=data.get('rol')
        )
        db.session.add(nuevo_apoderado)
        db.session.commit()
        return jsonify({'mensaje': 'Apoderado creado exitosamente'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Obtener todos los apoderados
@apoderado_bp.route('/apoderados', methods=['GET'])
def get_all_apoderados():
    apoderados = Apoderado.query.all()
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
    return jsonify({"apoderados": result})

# Obtener uno por ID
@apoderado_bp.route('/apoderados/<int:id>', methods=['GET'])
def get_apoderado(id):
    apoderado = Apoderado.query.get(id)
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

# Actualizar apoderado
@apoderado_bp.route('/apoderados/<int:id>', methods=['PUT'])
def update_apoderado(id):
    apoderado = Apoderado.query.get(id)
    if not apoderado:
        abort(404)
    data = request.get_json()
    try:
        apoderado.nombre_completo = data['nombre_completo']
        apoderado.rut = data['rut']
        apoderado.correo = data['correo']
        apoderado.password = data['password']
        apoderado.direccion = data['direccion']
        apoderado.numero_telefono = data['numero_telefono']
        apoderado.sexo = data.get('sexo')
        apoderado.rol = data.get('rol')
        db.session.commit()
        return jsonify({'mensaje': 'Apoderado actualizado exitosamente'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Eliminar apoderado
@apoderado_bp.route('/apoderados/<int:id>', methods=['DELETE'])
def delete_apoderado(id):
    apoderado = Apoderado.query.get(id)
    if not apoderado:
        abort(404)
    try:
        db.session.delete(apoderado)
        db.session.commit()
        return jsonify({'mensaje': 'Apoderado eliminado exitosamente'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400
