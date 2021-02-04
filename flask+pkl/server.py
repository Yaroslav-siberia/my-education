from flask import Flask,render_template, request, jsonify
import flask
import numpy as np
import traceback
import pickle
import pandas as pd
 
 
# App definition
app = Flask(__name__)
 
# importing models
with open('/home/toor/Projects/my-education/flask+pkl/model.pkl', 'rb') as f:
   classifier = pickle.load (f)
 
with open('/home/toor/Projects/my-education/flask+pkl/model_columns.pkl', 'rb') as f:
   model_columns = pickle.load (f)
 
 
@app.route('/')
def welcome():
   return "Boston Housing Price Prediction"
 
@app.route('/predict', methods=['POST','GET'])
def predict():
  
   if flask.request.method == 'GET':
       return "Prediction page"
 
   if flask.request.method == 'POST':
       try:
           json_ = request.json
           print(json_)
           query_ = pd.get_dummies(pd.DataFrame(json_))
           query = query_.reindex(columns = model_columns, fill_value= 0)
           prediction = list(classifier.predict(query))kp[
               
           ]
   app.run()