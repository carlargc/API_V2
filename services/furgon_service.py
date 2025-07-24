from models import db, Furgon, Sector, Colegio
from repositories.furgon_repository import (
    guardar,
    obtener_por_id,
    obtener_todos,
    actualizar,
    eliminar,
    filtrar
)

def crear_furgon(data):
    nuevo = Furgon(
        patente=data['patente'],
        marca=data['marca'],
        modelo=data['modelo'],
        ano=data['ano'],
        capacidad=data['capacidad'],
        cupos_disponibles=data['cupos_disponibles'],
        precio_base=data['precio_base'],
        validado=data['validado'],
        conductor_id=data['conductor_id'],
        sector_id=data['sector_id'],
        colegio_id=data['colegio_id']
    )
    db.session.add(nuevo)
    db.session.commit()
    return nuevo

def obtener_furgon(id):
    return Furgon.query.get(id)

def obtener_todos_furgones():
    return Furgon.query.all()

def actualizar_furgon(furgon, data):
    furgon.patente = data['patente']
    furgon.marca = data['marca']
    furgon.modelo = data['modelo']
    furgon.ano = data['ano']
    furgon.capacidad = data['capacidad']
    furgon.cupos_disponibles = data['cupos_disponibles']
    furgon.precio_base = data['precio_base']
    furgon.validado = data['validado']
    furgon.conductor_id = data['conductor_id']
    furgon.sector_id = data['sector_id']
    furgon.colegio_id = data['colegio_id']
    db.session.commit()

def eliminar_furgon(furgon):
    db.session.delete(furgon)
    db.session.commit()

def filtrar_furgones(comuna=None, colegio_id=None, poblacion=None):
    query = db.session.query(Furgon).join(Sector).join(Colegio)

    if comuna:
        query = query.filter(Sector.comuna == comuna)
    if colegio_id:
        query = query.filter(Furgon.colegio_id == colegio_id)
    if poblacion:
        query = query.filter(Sector.poblacion == poblacion)

    return query.all()
