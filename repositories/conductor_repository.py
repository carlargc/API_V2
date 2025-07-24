from models import db, Conductor

def crear_conductor_db(data):
    nuevo = Conductor(
        nombre_completo=data['nombre_completo'],
        rut=data['rut'],
        correo=data['correo'],
        numero_telefono=data.get('numero_telefono'),
        sexo=data['sexo'],
        rol=data['rol'],
        image=data.get('image')
    )
    db.session.add(nuevo)
    db.session.commit()
    return nuevo

def obtener_todos_conductores_db():
    return Conductor.query.all()

def obtener_conductor_por_id_db(id):
    return Conductor.query.get(id)

def actualizar_conductor_db(conductor, data):
    conductor.nombre_completo = data['nombre_completo']
    conductor.rut = data['rut']
    conductor.correo = data['correo']
    conductor.numero_telefono = data.get('numero_telefono')
    conductor.sexo = data['sexo']
    conductor.rol = data['rol']
    conductor.image = data.get('image')
    db.session.commit()
    return conductor

def eliminar_conductor_db(conductor):
    db.session.delete(conductor)
    db.session.commit()
    return conductor
