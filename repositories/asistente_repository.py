from models import db, Asistente

def get_asistente_by_id(id):
    return Asistente.query.get(id)

def get_all_asistentes():
    return Asistente.query.all()

def save_asistente(asistente):
    db.session.add(asistente)
    db.session.commit()
    return asistente

def update_asistente():
    db.session.commit()

def delete_asistente(asistente):
    db.session.delete(asistente)
    db.session.commit()
