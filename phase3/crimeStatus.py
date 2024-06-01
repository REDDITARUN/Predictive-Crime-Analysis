from flask import Blueprint, render_template, request, jsonify
import pickle
import numpy as np
from sklearn.preprocessing import LabelEncoder
import re
import random
import csv

crimeStatus = Blueprint('crimeStatus', __name__)

with open('knn_model.pkl', 'rb') as model_file:
    knn_model = pickle.load(model_file)

def load_encoder_mapping(csv_file_path):
    mapping = {}
    with open(csv_file_path, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for rows in reader:
            if len(rows) == 2 and rows[1].isdigit():
                mapping[rows[0]] = int(rows[1])
            else:
                print()
    return mapping

location_type_mapping = load_encoder_mapping("label_encoder_location_type_knn.csv")


@crimeStatus.route('/crimeStatus')
def home():
    return render_template('crimeStatus/crimeStatus.html')

@crimeStatus.route('/predictCrimeStatus', methods=['POST'])
def predict_crime_status():
    try:
        # Extracting form data
        time_occurred_str = request.form.get('Time_Occurred', '00:00')  # Default value if not provided
        time_match = re.match(r'(\d{1,2}):(\d{2})', time_occurred_str)
        if time_match:
            hours, minutes = map(int, time_match.groups())
            time_occurred = hours * 100 + minutes
        else:
            raise ValueError('Invalid time format. Use HH:MM.')

        area = int(request.form.get('Area', 0))
        area_name = int(request.form.get('Area_Name', 0))
        part_1_2=random.choice([1,2])
        reporting_district_number = int(request.form.get('Reporting_District_Number', 0))
        crime_code = int(request.form.get('Crime_Code', 0))
        victim_age = int(request.form.get('Victim_Age', 0))
        victim_sex = int(request.form.get('Victim_Sex', 0))
        victim_descent = int(request.form.get('Victim_Descent', 0))

        premise_code = float(request.form.get('Premise_Code', 0.0))
        latitude = float(request.form.get('Latitude', 0.0))
        longitude = float(request.form.get('Longitude', 0.0))

        location_type = request.form.get('Location_Type', 'Unknown')  # Default to 'Unknown'
        location_type_encoded = location_type_mapping.get(location_type, -1)  # Default to -1 if not found in mapping

        # Create the feature array
        features = np.array([[time_occurred, area, area_name, reporting_district_number, part_1_2, crime_code, victim_age, victim_sex, victim_descent, premise_code, latitude, longitude, location_type_encoded]])

        # Check if any value is NaN and handle it
        if np.isnan(features).any():
            raise ValueError("One or more feature values are missing or invalid.")

        # Predicting using the KNN model
        prediction = knn_model.predict(features)


        status_mapping = {
            0: "Criminal Arrested, Case Closed!",
            1: "Criminal Arrested, Decision Pending!",
            2: "Investigation in Progress, Complicated Case!",
        }

        prediction_label = status_mapping.get(prediction[0], "Unknown Status")
        status = f'The predicted crime status is: {prediction_label}'
        
        return render_template('crimeStatus/crimeStatus.html', prediction_status=status)
    except Exception as e:
        return jsonify({'error': str(e)}), 500