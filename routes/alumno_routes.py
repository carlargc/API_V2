from flask import Blueprint, jsonify, request
from models import db, Alumno
from datetime import datetime


alumno_bp = Blueprint('alumno_bp', __name__)

@alumno_bp.route('/alumnos', methods=['GET'])
def get_all_alumnos():
    alumnos = Alumno.query.all()
    result = []
    for alumno in alumnos:
        result.append({
            'id': alumno.id,
            'nombre_completo': alumno.nombre_completo,
            'rut': alumno.rut,
            'fecha_nacimiento': alumno.fecha_nacimiento.isoformat(),
            'horario_entrada': alumno.horario_entrada.isoformat(),
            'horario_salida': alumno.horario_salida.isoformat(),
            'curso': alumno.curso,
            'direccion_hogar': alumno.direccion_hogar,
            'nombre_contacto_emergencia': alumno.nombre_contacto_emergencia,
            'contacto_emergencia': alumno.contacto_emergencia,
            'colegio_id': alumno.colegio_id,
            'apoderado_id': alumno.apoderado_id,
            'sector_id': alumno.sector_id
        })
    return jsonify(result)


@alumno_bp.route('/alumnos', methods=['POST'])
def create_alumno():
    data = request.get_json()
    try:
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
        db.session.add(nuevo_alumno)
        db.session.commit()
        return jsonify({'mensaje': 'Alumno creado exitosamente'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400


@alumno_bp.route('/alumnos/<int:id>', methods=['DELETE'])
def delete_alumno(id):
    alumno = Alumno.query.get(id)
    if not alumno:
        abort(404)
    try:
        db.session.delete(alumno)
        db.session.commit()
        return jsonify({'mensaje': 'Alumno eliminado exitosamente'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400
    
    
@alumno_bp.route('/alumnos/<int:id>', methods=['PUT'])
def update_alumno(id):
    alumno = Alumno.query.get(id)
    if not alumno:
        abort(404)
    data = request.get_json()
    try:
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
        db.session.commit()
        return jsonify({'mensaje': 'Alumno actualizado exitosamente'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400
    
@alumno_bp.route('/alumnos/<int:id>', methods=['GET'])
def get_alumno(id):
    alumno = Alumno.query.get(id)
    if not alumno:
        abort(404)
    return jsonify({
        'id': alumno.id,
        'nombre_completo': alumno.nombre_completo,
        'rut': alumno.rut,
        'fecha_nacimiento': alumno.fecha_nacimiento.isoformat(),
        'horario_entrada': alumno.horario_entrada.isoformat(),
        'horario_salida': alumno.horario_salida.isoformat(),
        'curso': alumno.curso,
        'direccion_hogar': alumno.direccion_hogar,
        'nombre_contacto_emergencia': alumno.nombre_contacto_emergencia,
        'contacto_emergencia': alumno.contacto_emergencia,
        'colegio_id': alumno.colegio_id,
        'apoderado_id': alumno.apoderado_id,
        'sector_id': alumno.sector_id
    })
