from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__, template_folder='templates') #initializing a flask app
model = pickle.load(open('CKD.pkl', 'rb')) #loading the model

@app.route('/') #route to display the home page
def home():
    return render_template('home.html') #rendering the home page
@app.route('/Prediction', methods=['POST', 'GET'])

def prediction():
    return render_template('indexview.html')
@app.route('/Home', methods=['POST'])
def my_home():
    # Extract form values
    red_blood_cells = 1 if request.form['red_blood_cells'] == 'Normal' else 0
    pus_cell = 1 if request.form['pus_cell'] == 'Normal' else 0
    blood_glucose_random = float(request.form['blood_glucose_random'])
    blood_urea = float(request.form['blood_urea'])
    pedal_edema = 1 if request.form['pedal_edema'] == 'Yes' else 0
    anemia = 1 if request.form['anemia'] == 'Yes' else 0
    diabetesmellitus = 1 if request.form['diabetesmellitus'] == 'Yes' else 0
    coronary_artery_disease = 1 if request.form['coronary_artery_disease'] == 'Yes' else 0


    # Build input DataFrame
    features = np.array([[red_blood_cells, pus_cell, blood_glucose_random, blood_urea, pedal_edema, anemia,
                          diabetesmellitus, coronary_artery_disease]])

    columns = ['red_blood_cells','pus_cell','blood_glucose_random','blood_urea', 'pedal_edema', 'anemia',
               'diabetesmellitus', 'coronary_artery_disease']

    df = pd.DataFrame(features, columns=columns)

    # Make prediction
    output = model.predict(df)

    return render_template('result.html', pred=output[0])
if __name__ == '__main__':
    # running the app
    app.run(debug=True)
