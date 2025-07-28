from flask import Blueprint, request, jsonify, session
from services.auth_service import (
    registrar_apoderado,
    registrar_conductor,
    autenticar_usuario
)

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/registro-conductor', methods=['POST'])
def route_registrar_conductor():
    data = request.get_json()
    try:
        registrar_conductor(data)
        return jsonify({'mensaje': 'Conductor registrado exitosamente'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@auth_bp.route('/registro-apoderado', methods=['POST'])
def route_registrar_apoderado():
    data = request.get_json()
    try:
        registrar_apoderado(data)
        return jsonify({'mensaje': 'Apoderado registrado exitosamente'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    correo = data.get('correo')
    password = data.get('password')

    if not correo or not password:
        return jsonify({"error": "Correo y contraseña son necesarios"}), 400

    user, mensaje, status = autenticar_usuario(correo, password)
    if not user:
        return jsonify({"error": mensaje}), status

    session['user_id'] = user.id
    session['rol'] = user.rol
    session['nombre_completo'] = user.nombre_completo

    return jsonify({
        "mensaje": mensaje,
        "rol": user.rol,
        "nombre_completo": user.nombre_completo
    }), 200

@auth_bp.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({"mensaje": "Cierre de sesión exitoso"}), 200


