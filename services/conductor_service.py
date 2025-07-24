from repositories.conductor_repository import (
    crear_conductor_db,
    obtener_todos_conductores_db,
    obtener_conductor_por_id_db,
    actualizar_conductor_db,
    eliminar_conductor_db
)

def conductor_a_dict(conductor):
    return {
        "id": conductor.id,
        "nombre_completo": conductor.nombre_completo,
        "rut": conductor.rut,
        "correo": conductor.correo,
        "numero_telefono": conductor.numero_telefono,
        "sexo": conductor.sexo,
        "rol": conductor.rol
    }

def crear_conductor(data):
    return crear_conductor_db(data)

def obtener_conductores():
    conductores = obtener_todos_conductores_db()
    return [conductor_a_dict(c) for c in conductores]

def obtener_conductor_por_id(id):
    conductor = obtener_conductor_por_id_db(id)
    return conductor_a_dict(conductor) if conductor else None

def actualizar_conductor(id, data):
    conductor = obtener_conductor_por_id_db(id)
    if not conductor:
        return None
    return actualizar_conductor_db(conductor, data)

def eliminar_conductor(id):
    conductor = obtener_conductor_por_id_db(id)
    if not conductor:
        return None
    return eliminar_conductor_db(conductor)
