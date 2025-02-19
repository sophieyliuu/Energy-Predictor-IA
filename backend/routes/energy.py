from flask import Blueprint, request, jsonify
from models import db, EnergyReading
from datetime import datetime

energy_bp = Blueprint('energy', __name__)

@energy_bp.route('/add', methods=['POST'])
def add_energy_usage():
    data = request.json
    new_reading = EnergyReading(
        user_id=data['user_id'], 
        energy_usage=data['energy_usage'], 
        timestamp=datetime.utcnow()
    )
    db.session.add(new_reading)
    db.session.commit()
    return jsonify({'message': 'Energy usage recorded successfully'}), 201

@energy_bp.route('/get/<int:user_id>', methods=['GET'])
def get_energy_usage(user_id):
    readings = EnergyReading.query.filter_by(user_id=user_id).all()
    return jsonify([{
        'id': r.id,
        'timestamp': r.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
        'energy_usage': r.energy_usage
    } for r in readings])

@energy_bp.route('/delete/<int:reading_id>', methods=['DELETE'])
def delete_energy_usage(reading_id):
    reading = EnergyReading.query.get(reading_id)
    if not reading:
        return jsonify({'message': 'Energy record not found'}), 404
    
    db.session.delete(reading)
    db.session.commit()
    return jsonify({'message': 'Energy record deleted successfully'}), 200
