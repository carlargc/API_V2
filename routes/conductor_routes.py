from flask import Blueprint, request, jsonify
from models import db, Conductor

conductor_bp = Blueprint('conductor_bp', __name__)

@conductor_bp.route('/conductores', methods=['POST'])
def create_conductor():
    data = request.get_json()
    new_conductor = Conductor(
        nombre_completo=data['nombre_completo'],
        rut=data['rut'],
        correo=data['correo'],
        numero_telefono=data.get('numero_telefono'),
        sexo=data['sexo'],
        rol=data['rol'],
        image=data.get('image')
    )
    db.session.add(new_conductor)
    db.session.commit()
    return jsonify({"message": "Conductor creado exitosamente"}), 201

@conductor_bp.route('/conductores', methods=['GET'])
def get_conductores():
    conductores = Conductor.query.all()
    return jsonify({"conductores": [{
        "id": conductor.id,
        "nombre_completo": conductor.nombre_completo,
        "rut": conductor.rut,
        "correo": conductor.correo,
        "numero_telefono": conductor.numero_telefono,
        "sexo": conductor.sexo,
        "rol": conductor.rol
    } for conductor in conductores]})

@conductor_bp.route('/conductores/<int:id>', methods=['GET'])
def get_conductor(id):
    conductor = Conductor.query.get_or_404(id)
    return jsonify({
        "id": conductor.id,
        "nombre_completo": conductor.nombre_completo,
        "rut": conductor.rut,
        "correo": conductor.correo,
        "numero_telefono": conductor.numero_telefono,
        "sexo": conductor.sexo,
        "rol": conductor.rol
    })

@conductor_bp.route('/conductores/<int:id>', methods=['PUT'])
def update_conductor(id):
    data = request.get_json()
    conductor = Conductor.query.get_or_404(id)
    conductor.nombre_completo = data['nombre_completo']
    conductor.rut = data['rut']
    conductor.correo = data['correo']
    conductor.numero_telefono = data.get('numero_telefono')
    conductor.sexo = data['sexo']
    conductor.rol = data['rol']
    conductor.image = data.get('image')
    db.session.commit()
    return jsonify({"message": "Conductor actualizado exitosamente"})

@conductor_bp.route('/conductores/<int:id>', methods=['DELETE'])
def delete_conductor(id):
    conductor = Conductor.query.get_or_404(id)
    db.session.delete(conductor)
    db.session.commit()
    return jsonify({"message": "Conductor eliminado exitosamente"})

