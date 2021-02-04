from flask import Flask,Request,Response,jsonify
import requests
import pickle as pkl
import numpy as np
app = Flask(__name__)

with open('/home/toor/Projects/my-education//hw1.pkl', 'rb') as file:
    pickle_model = pkl.load(file)

@app.route('/predict', methods=['POST','GET'])
def predict():
  
   if Flask.request.method == 'GET':
       return "Prediction page"
 
   if Flask.request.method == 'POST':
       try:
           nums = np.array(request.json)
           print(json_)
           prediction = list(pickle_model.predict(nums))
 
           return jsonify({
               "prediction":str(prediction)
           })
 
       except:
           return jsonify({
               "trace": traceback.format_exc()
               })

@app.route('/add', methods=['POST'])
def add_func():
    num = requests.json.get('num')
    if num > 10:
        return 'too much',400
    else:
        return jsonify({'result':num+1})

if __name__ == '__main__':
    app.run('localhost', 5000)