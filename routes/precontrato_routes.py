from flask import Blueprint, jsonify
from services.precontrato_service import obtener_todos_precontratos_service

precontrato_bp = Blueprint('precontrato_bp', __name__)

@precontrato_bp.route('/precontratos', methods=['GET'])
def get_all_precontratos():
    precontratos = obtener_todos_precontratos_service()
    return jsonify(precontratos), 200
