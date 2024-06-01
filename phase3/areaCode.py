from flask import Flask, render_template, request, jsonify, Blueprint
import pickle
import traceback


areaCode = Blueprint('areaCode', __name__)

model_path = 'linear_regression_model.pkl'

with open(model_path, 'rb') as model_file:
    linear_model = pickle.load(model_file)

@areaCode.route('/areaCode')
def home():
    return render_template('areaCode/areaCode.html', predicted_area='')

@areaCode.route('/predictAreaCode', methods=['POST'])
def predict_area():
    try:
        latitude = float(request.form.get('latitude'))
        longitude = float(request.form.get('longitude'))
        predicted_area_code = round(linear_model.predict([[latitude, longitude]])[0])
        return render_template('areaCode/areaCode.html', predicted_area=predicted_area_code)
    except Exception as e:
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500
