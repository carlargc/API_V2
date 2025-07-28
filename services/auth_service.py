from models import db, Apoderado, Conductor
from repositories.auth_repository import buscar_apoderado_por_correo, buscar_conductor_por_correo
import bcrypt

from werkzeug.security import generate_password_hash

def registrar_apoderado(data):
    hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
    nuevo = Apoderado(
        nombre_completo=data['nombre_completo'],
        rut=data['rut'],
        correo=data['correo'],
        direccion=data['direccion'],
        numero_telefono=data['numero_telefono'],
        sexo=data['sexo'],
        rol='apoderado',
        password=hashed_password.decode('utf-8')
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
        password=bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
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

    if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
        return None, "Contraseña incorrecta", 401

    if user.rol not in ['ROLE_APODERADO', 'ROLE_CONDUCTOR']:
        return None, "Rol no permitido", 403

    return user, "Inicio de sesión exitoso", 200
