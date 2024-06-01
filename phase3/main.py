from flask import Flask, render_template, jsonify
from vehicleTheft import vehicleTheft
from crimeStatus import crimeStatus
from crimeCodeDesc import crimeCodeDesc
from contributeDetails import contributeDetails
import pandas as pd


app = Flask(__name__)
app.register_blueprint(vehicleTheft, url_prefix='/vehicleTheft')
app.register_blueprint(crimeStatus, url_prefix='/crimeStatus')
app.register_blueprint(crimeCodeDesc, url_prefix='/crimeCodeDesc')
app.register_blueprint(contributeDetails, url_prefix='/contributeDetails')

@app.route('/')
def index():
    crimeDF = pd.read_csv("crimeDF_cleaned_data.csv")
    crimeDF['Date_Reported'] = pd.to_datetime(crimeDF['Date_Reported'])
    crime_counts = crimeDF.groupby('Date_Reported').size().reset_index(name='count')
    crime_counts['Date_Reported'] = crime_counts['Date_Reported'].dt.strftime('%Y-%m-%d')
    data = crime_counts.to_dict(orient='records')
    return render_template('index.html', data=data)

@app.route('/data')
def data():
    # Similar data processing as above
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)