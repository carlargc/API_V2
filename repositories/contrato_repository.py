from models import db, Contrato, Colegio, Alumno, Apoderado, Furgon, Conductor

def obtener_colegio(id):
    return Colegio.query.get(id)

def obtener_alumno(id):
    return Alumno.query.get(id)

def obtener_apoderado(id):
    return Apoderado.query.get(id)

def obtener_furgon(id):
    return Furgon.query.get(id)

def obtener_conductor(id):
    return Conductor.query.get(id)

def guardar_contrato(contrato):
    db.session.add(contrato)
    db.session.commit()
    return contrato

def obtener_contrato_por_id(id):
    return Contrato.query.get(id)

def obtener_todos_los_contratos():
    return Contrato.query.all()

def eliminar_contrato_bd(contrato):
    db.session.delete(contrato)
    db.session.commit()
