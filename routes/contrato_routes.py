from flask import Blueprint, request, jsonify, abort
from models import db, Contrato, Colegio, Alumno, Apoderado, Furgon, Conductor
from datetime import date

contrato_bp = Blueprint('contrato_bp', __name__)

# Crear un nuevo contrato
@contrato_bp.route('/contrato', methods=['POST'])
def create_contrato():
    data = request.get_json()
    try:
        if not data:
            return jsonify({'error': 'El cuerpo de la solicitud está vacío o no es JSON válido'}), 400

        colegio = Colegio.query.get(data['id_colegio'])
        alumno = Alumno.query.get(data['id_alumno'])
        apoderado = Apoderado.query.get(data['id_apoderado'])
        furgon = Furgon.query.get(data['id_furgon'])
        conductor = Conductor.query.get(data['id_conductor'])

        nuevo_contrato = Contrato(
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
        db.session.add(nuevo_contrato)
        db.session.commit()
        return jsonify({'mensaje': 'Contrato creado exitosamente'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400


# Obtener un contrato por ID
@contrato_bp.route('/contrato/<int:id>', methods=['GET'])
def get_contrato(id):
    contrato = Contrato.query.get(id)
    if not contrato:
        abort(404)
    return jsonify({
        'id': contrato.id,
        'direccion_establecimiento': contrato.direccion_establecimiento,
        'direccion_hogar': contrato.direccion_hogar,
        'fecha_contratacion': contrato.fecha_contratacion.isoformat(),
        'nombre_alumno': contrato.nombre_alumno,
        'nombre_apoderado': contrato.nombre_apoderado,
        'rut_apoderado': contrato.rut_apoderado,
        'nombre_establecimiento': contrato.nombre_establecimiento,
        'periodo': contrato.periodo,
        'precio': contrato.precio,
        'estado': contrato.estado,
        'tipo_servicio': contrato.tipo_servicio,
        'nombre_contacto_emergencia': contrato.nombre_contacto_emergencia,
        'numero_contacto_emergencia': contrato.numero_contacto_emergencia,
        'furgon_id': contrato.furgon_id,
        'conductor_id': contrato.conductor_id,
        'apoderado_id': contrato.apoderado_id,
        'alumno_id': contrato.alumno_id,
        'colegio_id': contrato.colegio_id
    })


# Obtener todos los contratos
@contrato_bp.route('/contrato', methods=['GET'])
def get_all_contratos():
    contratos = Contrato.query.all()
    result = []
    for c in contratos:
        result.append({
            'id': c.id,
            'direccion_establecimiento': c.direccion_establecimiento,
            'direccion_hogar': c.direccion_hogar,
            'fecha_contratacion': c.fecha_contratacion.isoformat(),
            'nombre_alumno': c.nombre_alumno,
            'nombre_apoderado': c.nombre_apoderado,
            'rut_apoderado': c.rut_apoderado,
            'nombre_establecimiento': c.nombre_establecimiento,
            'periodo': c.periodo,
            'precio': c.precio,
            'estado': c.estado,
            'tipo_servicio': c.tipo_servicio,
            'nombre_contacto_emergencia': c.nombre_contacto_emergencia,
            'numero_contacto_emergencia': c.numero_contacto_emergencia,
            'furgon_id': c.furgon_id,
            'conductor_id': c.conductor_id,
            'apoderado_id': c.apoderado_id,
            'alumno_id': c.alumno_id,
            'colegio_id': c.colegio_id
        })
    return jsonify(result)


# Actualizar un contrato
@contrato_bp.route('/contrato/<int:id>', methods=['PUT'])
def update_contrato(id):
    contrato = Contrato.query.get(id)
    if not contrato:
        abort(404)
    data = request.get_json()
    try:
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
        db.session.commit()
        return jsonify({'mensaje': 'Contrato actualizado exitosamente'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400


# Eliminar un contrato
@contrato_bp.route('/contrato/<int:id>', methods=['DELETE'])
def delete_contrato(id):
    contrato = Contrato.query.get(id)
    if not contrato:
        abort(404)
    try:
        db.session.delete(contrato)
        db.session.commit()
        return jsonify({'mensaje': 'Contrato eliminado exitosamente'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400
