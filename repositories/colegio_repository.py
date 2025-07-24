from models import db, Colegio

def crear(data):
    colegio = Colegio(**data)
    db.session.add(colegio)
    db.session.commit()
    return colegio

def obtener_por_id(id):
    return Colegio.query.get(id)

def obtener_todos():
    return Colegio.query.all()

def actualizar(id, data):
    colegio = Colegio.query.get(id)
    if colegio:
        for key, value in data.items():
            setattr(colegio, key, value)
        db.session.commit()
    return colegio

def eliminar(id):
    colegio = Colegio.query.get(id)
    if colegio:
        db.session.delete(colegio)
        db.session.commit()
    return colegio
