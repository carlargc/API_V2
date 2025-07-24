from datetime import date
from models import Contrato
from repositories import contrato_repository as repo

def crear_contrato(data):
    colegio = repo.obtener_colegio(data['id_colegio'])
    alumno = repo.obtener_alumno(data['id_alumno'])
    apoderado = repo.obtener_apoderado(data['id_apoderado'])
    furgon = repo.obtener_furgon(data['id_furgon'])
    conductor = repo.obtener_conductor(data['id_conductor'])

    nuevo = Contrato(
        direccion_establecimiento=colegio.direccion,
        direccion_hogar=alumno.direccion_hogar,
        fecha_contratacion=date.today(),
        nombre_alumno=alumno.nombre_completo,
        nombre_apoderado=apoderado.nombre_completo,
        rut_apoderado=apoderado.rut,
        nombre_establecimiento=colegio.direccion,
        periodo=data['periodo'],
        precio=furgon.precio_base,
        estado=data['estado'],
        tipo_servicio=data['tipo_servicio'],
        nombre_contacto_emergencia=data['nombre_contacto_emergencia'],
        numero_contacto_emergencia=data['numero_contacto_emergencia'],
        furgon_id=furgon.id,
        conductor_id=conductor.id,
        apoderado_id=apoderado.id,
        alumno_id=alumno.id,
        colegio_id=colegio.id
    )

    return repo.guardar_contrato(nuevo)

def obtener_contrato(id):
    return repo.obtener_contrato_por_id(id)

def obtener_todos_contratos():
    return repo.obtener_todos_los_contratos()

def actualizar_contrato(contrato, data):
    contrato.direccion_establecimiento = data['direccion_establecimiento']
    contrato.direccion_hogar = data['direccion_hogar']
    contrato.nombre_alumno = data['nombre_alumno']
    contrato.nombre_apoderado = data['nombre_apoderado']
    contrato.rut_apoderado = data['rut_apoderado']
    contrato.nombre_establecimiento = data['nombre_establecimiento']
    contrato.periodo = data['periodo']
    contrato.precio = data['precio']
    contrato.estado = data['estado']
    contrato.tipo_servicio = data['tipo_servicio']
    contrato.nombre_contacto_emergencia = data['nombre_contacto_emergencia']
    contrato.numero_contacto_emergencia = data['numero_contacto_emergencia']
    contrato.furgon_id = data['furgon_id']
    contrato.conductor_id = data['conductor_id']
    contrato.apoderado_id = data['apoderado_id']
    contrato.alumno_id = data['alumno_id']
    contrato.colegio_id = data['colegio_id']
    return repo.guardar_contrato(contrato)

def eliminar_contrato(contrato):
    return repo.eliminar_contrato_bd(contrato)
