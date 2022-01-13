import flask
from flask import request
import numpy as np
import pickle

model = pickle.load(open('model/modelfp3.pkl', 'rb'))

app = flask.Flask(__name__, template_folder='templates')

@app.route('/')
def main():
    return(flask.render_template('main.html'))
if __name__ == '__main__':
    app.run(debug=True)

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    Usia = int(request.form['Usia'])
    Fraksi_ejeksi = int(request.form['Fraksi_ejeksi'])
    Kreatinin_serum = float(request.form['Kreatinin_serum'])
    Sodium_serum = float(request.form['Sodium_serum'])
    predict_list = [[Usia, Fraksi_ejeksi, Kreatinin_serum, Sodium_serum]]
    prediction = model.predict(predict_list)
    output = {0: 'Tidak Meninggal', 1: 'Meninggal'}
    return flask.render_template('main.html', prediction_text='Prediksi Pasien Gagal Jantung yaitu {}'.format(output[prediction[0]]))