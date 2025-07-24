from flask import Blueprint, request, jsonify, abort
from services.documento_service import (
    crear_documento,
    obtener_documento,
    obtener_todos_documentos,
    actualizar_documento,
    eliminar_documento
)

documento_bp = Blueprint('documento_bp', __name__)

@documento_bp.route('/documentos', methods=['POST'])
def create_documento():
    data = request.get_json()
    try:
        doc = crear_documento(data)
        return jsonify({'mensaje': 'Documento creado exitosamente', 'id': doc.id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@documento_bp.route('/documentos/<int:id>', methods=['GET'])
def get_documento(id):
    doc = obtener_documento(id)
    if not doc:
        abort(404)
    return jsonify({
        'id': doc.id,
        'contenido_documento': doc.contenido_documento.decode('utf-8') if doc.contenido_documento else None,
        'tipo_documento': doc.tipo_documento,
        'conductor_id': doc.conductor_id,
        'asistente_id': doc.asistente_id
    })

@documento_bp.route('/documentos', methods=['GET'])
def get_all_documentos():
    documentos = obtener_todos_documentos()
    return jsonify([{
        'id': doc.id,
        'contenido_documento': doc.contenido_documento.decode('utf-8') if doc.contenido_documento else None,
        'tipo_documento': doc.tipo_documento,
        'conductor_id': doc.conductor_id,
        'asistente_id': doc.asistente_id
    } for doc in documentos])

@documento_bp.route('/documentos/<int:id>', methods=['PUT'])
def update_documento(id):
    doc = obtener_documento(id)
    if not doc:
        abort(404)
    data = request.get_json()
    try:
        actualizar_documento(doc, data)
        return jsonify({'mensaje': 'Documento actualizado exitosamente'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@documento_bp.route('/documentos/<int:id>', methods=['DELETE'])
def delete_documento(id):
    doc = obtener_documento(id)
    if not doc:
        abort(404)
    try:
        eliminar_documento(doc)
        return jsonify({'mensaje': 'Documento eliminado exitosamente'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400
