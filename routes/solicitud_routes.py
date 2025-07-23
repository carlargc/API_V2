from flask import Blueprint, request, jsonify, abort
from models import db, Solicitud

solicitud_bp = Blueprint('solicitud_bp', __name__)

# Crear una nueva solicitud
@solicitud_bp.route('/solicitudes', methods=['POST'])
def create_solicitud():
    data = request.get_json()
    try:
        nueva = Solicitud(
            apoderado_id=data['apoderado_id'],
            conductor_id=data['conductor_id'],
            furgon_id=data['furgon_id'],
            aceptada=data.get('aceptada', False),
            rechazada=data.get('rechazada', False),
            vencida=data.get('vencida', False),
            estado=data.get('estado')
        )
        db.session.add(nueva)
        db.session.commit()
        return jsonify({'mensaje': 'Solicitud creada exitosamente'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Obtener una solicitud por ID
@solicitud_bp.route('/solicitudes/<int:id>', methods=['GET'])
def get_solicitud(id):
    solicitud = Solicitud.query.get(id)
    if not solicitud:
        abort(404)
    return jsonify({
        'id': solicitud.id,
        'apoderado_id': solicitud.apoderado_id,
        'conductor_id': solicitud.conductor_id,
        'furgon_id': solicitud.furgon_id,
        'aceptada': solicitud.aceptada,
        'rechazada': solicitud.rechazada,
        'vencida': solicitud.vencida,
        'estado': solicitud.estado
    })

# Obtener todas las solicitudes
@solicitud_bp.route('/solicitudes', methods=['GET'])
def get_all_solicitudes():
    solicitudes = Solicitud.query.all()
    return jsonify([{
        'id': s.id,
        'apoderado_id': s.apoderado_id,
        'conductor_id': s.conductor_id,
        'furgon_id': s.furgon_id,
        'aceptada': s.aceptada,
        'rechazada': s.rechazada,
        'vencida': s.vencida,
        'estado': s.estado
    } for s in solicitudes])

# Actualizar una solicitud
@solicitud_bp.route('/solicitudes/<int:id>', methods=['PUT'])
def update_solicitud(id):
    solicitud = Solicitud.query.get(id)
    if not solicitud:
        abort(404)
    data = request.get_json()
    try:
        solicitud.aceptada = data.get('aceptada', solicitud.aceptada)
        solicitud.rechazada = data.get('rechazada', solicitud.rechazada)
        solicitud.vencida = data.get('vencida', solicitud.vencida)
        solicitud.estado = data.get('estado', solicitud.estado)
        db.session.commit()
        return jsonify({'mensaje': 'Solicitud actualizada exitosamente'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Eliminar una solicitud
@solicitud_bp.route('/solicitudes/<int:id>', methods=['DELETE'])
def delete_solicitud(id):
    solicitud = Solicitud.query.get(id)
    if not solicitud:
        abort(404)
    try:
        db.session.delete(solicitud)
        db.session.commit()
        return jsonify({'mensaje': 'Solicitud eliminada exitosamente'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400
