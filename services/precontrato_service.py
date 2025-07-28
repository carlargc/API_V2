from repositories.precontrato_repository import obtener_todos_precontratos

def precontrato_a_dict(p):
    return {
        "id": p.id,
        "estado": p.estado,
        "periodo": p.periodo,
        "tipo_servicio": p.tipo_servicio,
        "fecha": p.fecha_contratacion.isoformat() if p.fecha_contratacion else None,
        "nombre_alumno": p.nombre_alumno,
        "nombre_apoderado": p.nombre_apoderado,
        "nombre_establecimiento": p.nombre_establecimiento,
        "precio": p.precio
    }

def obtener_todos_precontratos_service():
    precontratos = obtener_todos_precontratos()
    return [precontrato_a_dict(p) for p in precontratos]

