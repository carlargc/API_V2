from flask import Blueprint, request, jsonify
from models import Admin
from database import db

admin_bp = Blueprint('admin_bp', __name__)

# GET /inicio
@admin_bp.route('/inicio', methods=['GET'])
def inicio_admin():
    return jsonify({"mensaje": "Bienvenido al panel de administrador"}), 200

# GET /vista/<view> — vista simbólica
@admin_bp.route('/vista/<view>', methods=['GET'])
def obtener_vista(view):
    return jsonify({"vista": view, "mensaje": f"Renderizando vista: {view}"}), 200

# GET /correo/<correo> — obtener admin por correo
@admin_bp.route('/correo/<correo>', methods=['GET'])
def obtener_admin_por_correo(correo):
    admin = Admin.query.filter_by(correo=correo).first()
    if admin:
        return jsonify({
            "id": admin.id,
            "nombre": admin.nombre_completo,
            "correo": admin.correo
        }), 200
    return jsonify({"error": "Administrador no encontrado"}), 404

# PUT /administrador/<id> — actualizar admin
@admin_bp.route('/administrador/<int:id>', methods=['PUT'])
def actualizar_admin(id):
    admin = Admin.query.get(id)
    if not admin:
        return jsonify({"error": "Administrador no encontrado"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "Datos faltantes"}), 400

    admin.nombre_completo = data.get('nombre_completo', admin.nombre_completo)
    admin.correo = data.get('correo', admin.correo)
    # admin.password = data.get('password', admin.password)  # si deseas permitir cambio

    db.session.commit()
    return jsonify({"mensaje": "Administrador actualizado"}), 200

# GET /administrador — listar todos los admins
@admin_bp.route('/administrador', methods=['GET'])
def listar_administradores():
    admins = Admin.query.all()
    return jsonify([
        {
            "id": admin.id,
            "nombre": admin.nombre_completo,
            "correo": admin.correo
        } for admin in admins
    ]), 200

# POST /administrador — crear nuevo admin
@admin_bp.route('/administrador', methods=['POST'])
def crear_admin():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Datos requeridos"}), 400

    nuevo_admin = Admin(
        nombre_completo=data.get('nombre_completo'),
        correo=data.get('correo'),
        password=data.get('password')  # En producción deberías hashear la contraseña
    )

    db.session.add(nuevo_admin)
    db.session.commit()
    return jsonify({"mensaje": "Administrador creado", "id": nuevo_admin.id}), 201


# DELETE /administrador/<id> — eliminar admin
@admin_bp.route('/administrador/<int:id>', methods=['DELETE'])
def eliminar_admin(id):
    admin = Admin.query.get(id)
    if not admin:
        return jsonify({"error": "Administrador no encontrado"}), 404

    db.session.delete(admin)
    db.session.commit()
    return jsonify({"mensaje": f"Administrador con ID {id} eliminado correctamente"}), 200