from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from models import Apoderado, Conductor, db
import bcrypt
from werkzeug.security import check_password_hash
from flask import session   


auth_bp = Blueprint('auth_bp', __name__)

#Registros de apoderado, conductor 

@auth_bp.route('/registro-conductor', methods=['POST'])
def registrar_conductor():
    data = request.get_json()
    try:
        nuevo_conductor = Conductor(
            nombre_completo=data['nombre_completo'],
            rut=data['rut'],
            correo=data['correo'],
            numero_telefono=data['numero_telefono'],
            sexo=data.get('sexo'),
            rol="ROLE_CONDUCTOR",  # Rol fijo
            password=generate_password_hash(data['password'])  # Encripta la contraseña
        )
        db.session.add(nuevo_conductor)
        db.session.commit()
        return jsonify({'mensaje': 'Conductor registrado exitosamente'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400
    
# Registro de apoderado
@auth_bp.route('/registro-apoderado', methods=['POST'])
def registrar_apoderado():
    data = request.get_json()
    try:
        nuevo_apoderado = Apoderado(
            nombre_completo=data['nombre_completo'],
            rut=data['rut'],
            correo=data['correo'],
            direccion=data['direccion'],
            sexo=data.get('sexo'),
            numero_telefono=data['numero_telefono'],
            rol="ROLE_APODERADO",
            password=generate_password_hash(data['password'])
        )
        db.session.add(nuevo_apoderado)
        db.session.commit()
        return jsonify({'mensaje': 'Apoderado registrado exitosamente'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400
    
    
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    correo = data.get('correo')
    password = data.get('password')

    if not correo or not password:
        return jsonify({"error": "Correo y contraseña son necesarios"}), 400

    apoderado = Apoderado.query.filter_by(correo=correo).first()
    conductor = Conductor.query.filter_by(correo=correo).first()
    user = apoderado or conductor

    if not user:
        return jsonify({"error": "Usuario no encontrado"}), 404

    if not check_password_hash(user.password, password):
        return jsonify({"error": "Contraseña incorrecta"}), 401

    if user.rol not in ['ROLE_APODERADO', 'ROLE_CONDUCTOR']:
        return jsonify({"error": "Rol no permitido"}), 403

    session['user_id'] = user.id
    session['rol'] = user.rol
    session['nombre_completo'] = user.nombre_completo

    return jsonify({
        "mensaje": "Inicio de sesión exitoso",
        "rol": user.rol,
        "nombre_completo": user.nombre_completo
    }), 200

@auth_bp.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({"mensaje": "Cierre de sesión exitoso"}), 200