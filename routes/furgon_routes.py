from flask import Blueprint, request, jsonify, abort
from models import db, Furgon

furgon_bp = Blueprint('furgon_bp', __name__)

@furgon_bp.route('/furgones', methods=['POST'])
def create_furgon():
    data = request.get_json()
    try:
        nuevo_furgon = Furgon(
            patente=data['patente'],
            marca=data['marca'],
            modelo=data['modelo'],
            ano=data['ano'],
            capacidad=data['capacidad'],
            cupos_disponibles=data['cupos_disponibles'],
            precio_base=data['precio_base'],
            validado=data['validado'],
            conductor_id=data['conductor_id'],
            sector_id=data['sector_id'],
            colegio_id=data['colegio_id']
        )
        db.session.add(nuevo_furgon)
        db.session.commit()
        return jsonify({'mensaje': 'Furgón creado exitosamente'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@furgon_bp.route('/furgones/<int:id>', methods=['GET'])
def get_furgon(id):
    furgon = Furgon.query.get(id)
    if not furgon:
        abort(404)
    return jsonify({
        'id': furgon.id,
        'patente': furgon.patente,
        'marca': furgon.marca,
        'modelo': furgon.modelo,
        'ano': furgon.ano,
        'capacidad': furgon.capacidad,
        'cupos_disponibles': furgon.cupos_disponibles,
        'precio_base': furgon.precio_base,
        'validado': furgon.validado,
        'conductor_id': furgon.conductor_id,
        'sector_id': furgon.sector_id,
        'colegio_id': furgon.colegio_id
    })

@furgon_bp.route('/furgones', methods=['GET'])
def get_all_furgones():
    furgones = Furgon.query.all()
    result = []
    for furgon in furgones:
        result.append({
            'id': furgon.id,
            'patente': furgon.patente,
            'marca': furgon.marca,
            'modelo': furgon.modelo,
            'ano': furgon.ano,
            'capacidad': furgon.capacidad,
            'cupos_disponibles': furgon.cupos_disponibles,
            'precio_base': furgon.precio_base,
            'validado': furgon.validado,
            'conductor_id': furgon.conductor_id,
            'sector_id': furgon.sector_id,
            'colegio_id': furgon.colegio_id
        })
    return jsonify(result)

@furgon_bp.route('/furgones/<int:id>', methods=['PUT'])
def update_furgon(id):
    furgon = Furgon.query.get(id)
    if not furgon:
        abort(404)
    data = request.get_json()
    try:
        furgon.patente = data['patente']
        furgon.marca = data['marca']
        furgon.modelo = data['modelo']
        furgon.ano = data['ano']
        furgon.capacidad = data['capacidad']
        furgon.cupos_disponibles = data['cupos_disponibles']
        furgon.precio_base = data['precio_base']
        furgon.validado = data['validado']
        furgon.conductor_id = data['conductor_id']
        furgon.sector_id = data['sector_id']
        furgon.colegio_id = data['colegio_id']
        db.session.commit()
        return jsonify({'mensaje': 'Furgón actualizado exitosamente'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@furgon_bp.route('/furgones/<int:id>', methods=['DELETE'])
def delete_furgon(id):
    furgon = Furgon.query.get(id)
    if not furgon:
        abort(404)
    try:
        db.session.delete(furgon)
        db.session.commit()
        return jsonify({'mensaje': 'Furgón eliminado exitosamente'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400



@furgon_bp.route('/furgones', methods=['GET'])
def obtener_furgones_filtrados():
    comuna = request.args.get('comuna')
    colegio_id = request.args.get('colegio')
    poblacion = request.args.get('poblacion')

    query = db.session.query(Furgon).join(Sector).join(Colegio)

    if comuna:
        query = query.filter(Sector.comuna == comuna)
    if colegio_id:
        query = query.filter(Furgon.colegio_id == colegio_id)
    if poblacion:
        query = query.filter(Sector.poblacion == poblacion)

    furgones = query.all()

    return jsonify({
        "furgones": [{
            "id": f.id,
            "patente": f.patente,
            "marca": f.marca,
            "modelo": f.modelo,
            "ano": f.ano,
            "capacidad": f.capacidad,
            "cupos_disponibles": f.cupos_disponibles,
            "precio_base": f.precio_base,
            "validado": f.validado,
            "sector_id": f.sector_id,
            "colegio_id": f.colegio_id,
            "conductor_id": f.conductor_id
        } for f in furgones]
    }), 200