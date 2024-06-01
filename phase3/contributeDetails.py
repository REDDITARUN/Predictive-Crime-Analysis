from flask import Blueprint, Flask, render_template, request
import csv
contributeDetails = Blueprint('contributeDetails', __name__)


def load_encoder_mapping(csv_file_path):
    mapping = {}
    with open(csv_file_path, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for rows in reader:
            if len(rows) == 2 and rows[1].isdigit():
                mapping[rows[0]] = int(rows[1])
    return mapping

crime_description_mapping = load_encoder_mapping("label_encoder_crime_description.csv")

@contributeDetails.route('/contributeDetails')
def home():
    return render_template('contributeDetails/contributeDetails.html', crime_description_mapping=crime_description_mapping)

@contributeDetails.route('/submitContributeDetails', methods=['POST'])
def submit_contribute_details():
    if request.method == 'POST':
        date_reported = request.form['date_reported']
        date_occurred = request.form['date_occurred']
        time_occurred = request.form['time_occurred']
        area = request.form['Area']
        area_name = request.form['Area_Name']
        reporting_district_number = request.form['Reporting_District_Number']
        part_1_or_2 = request.form['part_1_or_2']
        crime_code = request.form['Crime_Code']
        crime_code_description = request.form['Crime_code_description']
        victim_age = request.form['victim_age']
        victim_sex = request.form['victim_sex']
        victim_descent = request.form['victim_descent']
        premise_code = request.form['Premise_Code']
        premise_description = request.form['premise_description']
        status_description = request.form['status_description']
        latitude = request.form['Latitude']
        longitude = request.form['Longitude']
        location_type = request.form['Location_Type']

        # store them in a database

        return render_template('contributeDetails/contributeDetails.html', results="Form Submitted Successfully!", )
