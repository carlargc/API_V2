from flask import Blueprint, request, jsonify, abort
from models import db, Documentos

documento_bp = Blueprint('documento_bp', __name__)

# Crear un nuevo documento
@documento_bp.route('/documentos', methods=['POST'])
def create_documento():
    data = request.get_json()
    try:
        nuevo_documento = Documentos(
            contenido_documento=data['contenido_documento'].encode('utf-8'),
            tipo_documento=data['tipo_documento'],
            conductor_id=data.get('conductor_id'),
            asistente_id=data.get('asistente_id')
        )
        db.session.add(nuevo_documento)
        db.session.commit()
        return jsonify({'mensaje': 'Documento creado exitosamente'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Obtener un documento por ID
@documento_bp.route('/documentos/<int:id>', methods=['GET'])
def get_documento(id):
    documento = Documentos.query.get(id)
    if not documento:
        abort(404)
    return jsonify({
        'id': documento.id,
        'contenido_documento': documento.contenido_documento.decode('utf-8') if documento.contenido_documento else None,
        'tipo_documento': documento.tipo_documento,
        'conductor_id': documento.conductor_id,
        'asistente_id': documento.asistente_id
    })

# Obtener todos los documentos
@documento_bp.route('/documentos', methods=['GET'])
def get_all_documentos():
    documentos = Documentos.query.all()
    return jsonify([{
        'id': doc.id,
        'contenido_documento': doc.contenido_documento.decode('utf-8') if doc.contenido_documento else None,
        'tipo_documento': doc.tipo_documento,
        'conductor_id': doc.conductor_id,
        'asistente_id': doc.asistente_id
    } for doc in documentos])

# Actualizar un documento
@documento_bp.route('/documentos/<int:id>', methods=['PUT'])
def update_documento(id):
    documento = Documentos.query.get(id)
    if not documento:
        abort(404)
    data = request.get_json()
    try:
        documento.tipo_documento = data['tipo_documento']
        documento.contenido_documento = data['contenido_documento'].encode('utf-8')
        db.session.commit()
        return jsonify({'mensaje': 'Documento actualizado exitosamente'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Eliminar un documento
@documento_bp.route('/documentos/<int:id>', methods=['DELETE'])
def delete_documento(id):
    documento = Documentos.query.get(id)
    if not documento:
        abort(404)
    try:
        db.session.delete(documento)
        db.session.commit()
        return jsonify({'mensaje': 'Documento eliminado exitosamente'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400
