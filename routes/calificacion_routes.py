from flask import Blueprint, request, jsonify, abort
from models import db, Calificacion

calificacion_bp = Blueprint('calificacion_bp', __name__)

# Crear una nueva calificación
@calificacion_bp.route('/calificaciones', methods=['POST'])
def create_calificacion():
    data = request.get_json()
    try:
        nueva = Calificacion(
            apoderado_id=data['apoderado_id'],
            conductor_id=data['conductor_id'],
            contrato_id=data['contrato_id'],
            puntuacion=data['puntuacion'],
            comentario=data.get('comentario')
        )
        db.session.add(nueva)
        db.session.commit()
        return jsonify({'mensaje': 'Calificación creada exitosamente'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Obtener una calificación por ID
@calificacion_bp.route('/calificaciones/<int:id>', methods=['GET'])
def get_calificacion(id):
    calificacion = Calificacion.query.get(id)
    if not calificacion:
        abort(404)
    return jsonify({
        'id': calificacion.id,
        'apoderado_id': calificacion.apoderado_id,
        'conductor_id': calificacion.conductor_id,
        'contrato_id': calificacion.contrato_id,
        'puntuacion': calificacion.puntuacion,
        'comentario': calificacion.comentario,
        'fecha_calificacion': calificacion.fecha_calificacion.isoformat()
    })

# Obtener todas las calificaciones
@calificacion_bp.route('/calificaciones', methods=['GET'])
def get_all_calificaciones():
    calificaciones = Calificacion.query.all()
    return jsonify([{
        'id': c.id,
        'apoderado_id': c.apoderado_id,
        'conductor_id': c.conductor_id,
        'contrato_id': c.contrato_id,
        'puntuacion': c.puntuacion,
        'comentario': c.comentario,
        'fecha_calificacion': c.fecha_calificacion.isoformat()
    } for c in calificaciones])

# Actualizar una calificación
@calificacion_bp.route('/calificaciones/<int:id>', methods=['PUT'])
def update_calificacion(id):
    calificacion = Calificacion.query.get(id)
    if not calificacion:
        abort(404)
    data = request.get_json()
    try:
        calificacion.puntuacion = data['puntuacion']
        calificacion.comentario = data.get('comentario')
        db.session.commit()
        return jsonify({'mensaje': 'Calificación actualizada exitosamente'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Eliminar una calificación
@calificacion_bp.route('/calificaciones/<int:id>', methods=['DELETE'])
def delete_calificacion(id):
    calificacion = Calificacion.query.get(id)
    if not calificacion:
        abort(404)
    try:
        db.session.delete(calificacion)
        db.session.commit()
        return jsonify({'mensaje': 'Calificación eliminada exitosamente'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400
