# services/alumno_service.py

from datetime import datetime
from models import Alumno
import repositories.alumno_repository as repo


def obtener_todos_alumnos():
    return repo.obtener_todos()

def obtener_alumno_por_id(id):
    return repo.obtener_por_id(id)

def crear_alumno(data):
    nuevo_alumno = Alumno(
        nombre_completo=data['nombre_completo'],
        rut=data['rut'],
        fecha_nacimiento=datetime.strptime(data['fecha_nacimiento'], '%Y-%m-%d').date(),
        horario_entrada=datetime.strptime(data['horario_entrada'], '%H:%M').time(),
        horario_salida=datetime.strptime(data['horario_salida'], '%H:%M').time(),
        curso=data['curso'],
        direccion_hogar=data.get('direccion_hogar'),
        nombre_contacto_emergencia=data.get('nombre_contacto_emergencia'),
        contacto_emergencia=data['contacto_emergencia'],
        colegio_id=data['colegio_id'],
        apoderado_id=data['apoderado_id'],
        sector_id=data['sector_id']
    )
    return repo.guardar(nuevo_alumno)

def actualizar_alumno(alumno, data):
    alumno.nombre_completo = data['nombre_completo']
    alumno.rut = data['rut']
    alumno.fecha_nacimiento = datetime.strptime(data['fecha_nacimiento'], '%Y-%m-%d').date()
    alumno.horario_entrada = datetime.strptime(data['horario_entrada'], '%H:%M').time()
    alumno.horario_salida = datetime.strptime(data['horario_salida'], '%H:%M').time()
    alumno.curso = data['curso']
    alumno.direccion_hogar = data.get('direccion_hogar')
    alumno.nombre_contacto_emergencia = data.get('nombre_contacto_emergencia')
    alumno.contacto_emergencia = data['contacto_emergencia']
    alumno.colegio_id = data['colegio_id']
    alumno.apoderado_id = data['apoderado_id']
    alumno.sector_id = data['sector_id']
    repo.actualizar()
    return alumno

def eliminar_alumno(alumno):
    repo.eliminar(alumno)

def obtener_alumnos_por_apoderado(apoderado_id):
    return Alumno.query.filter_by(apoderado_id=apoderado_id).all()
