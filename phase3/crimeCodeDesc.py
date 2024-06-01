from flask import Blueprint, render_template, request
import pandas as pd
import numpy as np
import pickle
import csv
import re

crimeCodeDesc = Blueprint('crimeCodeDesc', __name__)
with open('xgb_classifier_crime_desc.pkl', 'rb') as model_file:
    xgb_classifier = pickle.load(model_file)


def load_encoder_mapping(csv_file_path):
    mapping = {}
    with open(csv_file_path, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for rows in reader:
            if len(rows) == 2 and rows[1].isdigit():
                mapping[rows[0]] = int(rows[1])
    return mapping

crime_description_mapping = load_encoder_mapping("label_encoder_crime_description.csv")
location_type_mapping = load_encoder_mapping("label_encoder_location_type_xgb.csv")

@crimeCodeDesc.route('/crimeCodeDesc')
def home():
    return render_template('crimeCodeDesc/crimeCodeDesc.html')

@crimeCodeDesc.route('/predictCrimeCodeDesc', methods=['POST'])
def predict_crime_code_desc():
    try:
        time_occurred_str = request.form.get('Time_Occurred')
        time_match = re.match(r'(\d{1,2}):(\d{2})', time_occurred_str)
        if time_match:
            hours, minutes = map(int, time_match.groups())
            time_occurred = hours * 100 + minutes
        else:
            raise ValueError('Invalid time format. Use HH:MM.')

        premise_code = float(request.form.get('Premise_Code'))
        area = int(request.form.get('Area'))
        location_type = request.form.get('Location_Type')
        location_type_encoded = location_type_mapping.get(location_type)
        features = np.array([[time_occurred, premise_code, area, location_type_encoded]])
        prediction_encoded = xgb_classifier.predict(features)
        prediction = None
        for key, value in crime_description_mapping.items():
            if value == prediction_encoded[0]:
                prediction = key
                break
        return render_template('crimeCodeDesc/crimeCodeDesc.html', prediction=prediction)
    except Exception as e:
        return str(e), 500
