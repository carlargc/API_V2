from models import db, Apoderado, Conductor
from werkzeug.security import generate_password_hash, check_password_hash
from repositories.auth_repository import buscar_apoderado_por_correo, buscar_conductor_por_correo

def registrar_apoderado(data):
    nuevo = Apoderado(
        nombre_completo=data['nombre_completo'],
        rut=data['rut'],
        correo=data['correo'],
        direccion=data['direccion'],
        sexo=data.get('sexo'),
        numero_telefono=data['numero_telefono'],
        rol="ROLE_APODERADO",
        password=generate_password_hash(data['password'])
    )
    db.session.add(nuevo)
    db.session.commit()
    return nuevo

def registrar_conductor(data):
    nuevo = Conductor(
        nombre_completo=data['nombre_completo'],
        rut=data['rut'],
        correo=data['correo'],
        numero_telefono=data['numero_telefono'],
        sexo=data.get('sexo'),
        rol="ROLE_CONDUCTOR",
        password=generate_password_hash(data['password'])
    )
    db.session.add(nuevo)
    db.session.commit()
    return nuevo

def autenticar_usuario(correo, password):
    apoderado = buscar_apoderado_por_correo(correo)
    conductor = buscar_conductor_por_correo(correo)
    user = apoderado or conductor

    if not user:
        return None, "Usuario no encontrado", 404

    if not check_password_hash(user.password, password):
        return None, "Contraseña incorrecta", 401

    if user.rol not in ['ROLE_APODERADO', 'ROLE_CONDUCTOR']:
        return None, "Rol no permitido", 403

    return user, "Inicio de sesión exitoso", 200
