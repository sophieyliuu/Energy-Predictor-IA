from flask import Blueprint, request, jsonify
from models import db, EnergyReading, Prediction
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta

predictions_bp = Blueprint('predictions', __name__)

@predictions_bp.route('/generate/<int:user_id>', methods=['GET'])
def generate_prediction(user_id):
    readings = EnergyReading.query.filter_by(user_id=user_id).all()
    if len(readings) < 2:
        return jsonify({'message': 'Not enough data for prediction'}), 400
    
    df = pd.DataFrame([(r.timestamp.timestamp(), r.energy_usage) for r in readings], columns=['timestamp', 'energy_usage'])
    df = df.sort_values('timestamp')
    X = df[['timestamp']]
    y = df['energy_usage']
    model = LinearRegression()
    model.fit(X, y)
    
    future_timestamp = datetime.utcnow().timestamp() + 86400  # Predict for the next day
    prediction_value = model.predict(np.array([[future_timestamp]]))[0]
    
    new_prediction = Prediction(user_id=user_id, predicted_usage=prediction_value, timestamp=datetime.utcnow())
    db.session.add(new_prediction)
    db.session.commit()
    
    return jsonify({'predicted_usage': prediction_value})

@predictions_bp.route('/get/<int:user_id>', methods=['GET'])
def get_predictions(user_id):
    predictions = Prediction.query.filter_by(user_id=user_id).all()
    return jsonify([{
        'id': p.id,
        'timestamp': p.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
        'predicted_usage': p.predicted_usage
    } for p in predictions])
