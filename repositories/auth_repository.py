from models import Apoderado, Conductor

def buscar_apoderado_por_correo(correo):
    return Apoderado.query.filter_by(correo=correo).first()

def buscar_conductor_por_correo(correo):
    return Conductor.query.filter_by(correo=correo).first()
