from models import db, Furgon, Sector, Colegio

def guardar(furgon):
    db.session.add(furgon)
    db.session.commit()
    return furgon

def obtener_por_id(id):
    return Furgon.query.get(id)

def obtener_todos():
    return Furgon.query.all()

def actualizar():
    db.session.commit()

def eliminar(furgon):
    db.session.delete(furgon)
    db.session.commit()

def filtrar(comuna=None, colegio_id=None, poblacion=None):
    query = db.session.query(Furgon).join(Sector).join(Colegio)

    if comuna:
        query = query.filter(Sector.comuna == comuna)
    if colegio_id:
        query = query.filter(Furgon.colegio_id == colegio_id)
    if poblacion:
        query = query.filter(Sector.poblacion == poblacion)

    return query.all()
