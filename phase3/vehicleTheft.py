from flask import Blueprint, render_template, request, jsonify
import pickle
import numpy as np
import random
import re
from sklearn.preprocessing import StandardScaler

vehicleTheft = Blueprint('vehicleTheft', __name__)
with open('logistic_regression_model.pkl', 'rb') as model_file:
    logistic_model = pickle.load(model_file)

scaler = StandardScaler()

@vehicleTheft.route('/vehicleTheft')
def home():
    return render_template('vehicleTheft/vehicleTheft.html')

@vehicleTheft.route('/predictVehicleTheft', methods=['POST'])
def predict_vehicle_theft():
    try:
        time_occurred_str = request.form.get('time_now')
        time_match = re.match(r'(\d{1,2}):(\d{2})', time_occurred_str)
        if time_match:
            hours, minutes = map(int, time_match.groups())
            time_occurred = hours * 100 + minutes
        else:
            raise ValueError('Invalid time format. Use HH:MM.')

        area = float(request.form.get('Area'))
        victim_age = random.randint(20, 70)
        premise_code = float(request.form.get('Premise_Code'))

        features = np.array([[time_occurred, area, victim_age, premise_code]])

        prediction = logistic_model.predict(features)
        is_vehicle_theft = 'Your Vehicle might be at risk!' if prediction[0] == 1 else 'No risk in this locality'
        # is_vehicle_theft = random.choice()
        return render_template('vehicleTheft/vehicleTheft.html', prediction=is_vehicle_theft)

    except Exception as e:
        return jsonify({'error': str(e)}), 500
