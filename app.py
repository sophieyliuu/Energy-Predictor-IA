from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import datetime

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///energy_usage.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# Import route blueprints
from routes.auth import auth_bp
from routes.energy import energy_bp
from routes.predictions import predictions_bp

# Register Blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(energy_bp, url_prefix='/energy')
app.register_blueprint(predictions_bp, url_prefix='/predict')

@app.route('/')
def home():
    return jsonify({'message': 'Energy Usage Predictor API is running'})

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
