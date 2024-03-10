from flask import Flask,render_template,url_for,request
import pandas as pd 
import numpy as np
import pickle

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        density = request.form['message']
        data = [density]
        data = cv.transform(data)
        my_prediction = clf.predict(data)
    return render_template('result.html',prediction = my_prediction)

if __name__ == '__main__':
	##load vectorizer and model
	with open('model/linearReg.pkl', 'rb') as f:
	    cv, clf = pickle.load(f)
	
	app.run(host='0.0.0.0',port=5000)
