from flask import Blueprint, request, jsonify, abort
from models import db, Notificacion

notificacion_bp = Blueprint('notificacion_bp', __name__)

@notificacion_bp.route('/notificaciones', methods=['POST'])
def create_notificacion():
    data = request.get_json()
    try:
        nueva_notificacion = Notificacion(
            mensaje=data['mensaje'],
            conductor_destino_id=data.get('conductor_destino_id'),
            apoderado_destino_id=data.get('apoderado_destino_id')
        )
        db.session.add(nueva_notificacion)
        db.session.commit()
        return jsonify({'mensaje': 'Notificación creada exitosamente'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@notificacion_bp.route('/notificaciones/<int:id>', methods=['GET'])
def get_notificacion(id):
    notificacion = Notificacion.query.get(id)
    if not notificacion:
        abort(404)
    return jsonify({
        'id': notificacion.id,
        'mensaje': notificacion.mensaje,
        'fecha': notificacion.fecha.isoformat(),
        'conductor_destino_id': notificacion.conductor_destino_id,
        'apoderado_destino_id': notificacion.apoderado_destino_id
    })

@notificacion_bp.route('/notificaciones', methods=['GET'])
def get_all_notificaciones():
    notificaciones = Notificacion.query.all()
    return jsonify([{
        'id': n.id,
        'mensaje': n.mensaje,
        'fecha': n.fecha.isoformat(),
        'conductor_destino_id': n.conductor_destino_id,
        'apoderado_destino_id': n.apoderado_destino_id
    } for n in notificaciones])

@notificacion_bp.route('/notificaciones/<int:id>', methods=['DELETE'])
def delete_notificacion(id):
    notificacion = Notificacion.query.get(id)
    if not notificacion:
        abort(404)
    try:
        db.session.delete(notificacion)
        db.session.commit()
        return jsonify({'mensaje': 'Notificación eliminada exitosamente'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400