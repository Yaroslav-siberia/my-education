from flask import Flask,Request,Response,jsonify
import requests
import datetime
app = Flask(__name__)

@app.route('/time')
def current_time():
    return {'time': datetime.datetime.now()}

@app.route('/add', methods=['POST'])
def add_func():
    num = requests.json.get('num')
    if num > 10:
        return 'too much',400
    else:
        return jsonify({'result':num+1})

if __name__ == '__main__':
    app.run('localhost', 5000)