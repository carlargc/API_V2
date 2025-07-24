from models import db, Documentos

def guardar_documento(documento):
    db.session.add(documento)
    db.session.commit()
    return documento

def obtener_documento_por_id(id):
    return Documentos.query.get(id)

def obtener_todos():
    return Documentos.query.all()

def eliminar_documento(documento):
    db.session.delete(documento)
    db.session.commit()
