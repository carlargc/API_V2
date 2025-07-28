from repositories import colegio_repository

def colegio_a_dict(colegio):
    return {
        'id': colegio.id,
        'rbd': colegio.rbd,
       'nombre': colegio.nombre,
        'direccion': colegio.direccion,
        'contacto': colegio.contacto,
        'sector_id': colegio.sector_id
    }

def crear_colegio(data):
    colegio = colegio_repository.crear(data)
    return colegio

def obtener_colegio_por_id(id):
    colegio = colegio_repository.obtener_por_id(id)
    return colegio_a_dict(colegio) if colegio else None

def obtener_todos_los_colegios():
    colegios = colegio_repository.obtener_todos()
    return [colegio_a_dict(c) for c in colegios]

def actualizar_colegio(id, data):
    colegio = colegio_repository.actualizar(id, data)
    return colegio

def eliminar_colegio(id):
    colegio = colegio_repository.eliminar(id)
    return colegio
