from difference import Difference
from position import Position
from flask import request
from flask import Flask
import json

app = Flask(__name__)
posicion = Position()
diferencia = Difference()

@app.route('/', methods = ['GET', 'POST'])
def api_root():
    return 'Position service'

@app.route('/service', methods = ['POST'])
def set_position():
    content = request.get_json()
    posicion.name = content['name']
    posicion.x = content['x']
    posicion.y = content['y']
    return "Set position"

@app.route('/position', methods = ['GET'])
def get_position():
    obj = {
        "name": posicion.name,
        "x": posicion.x,
        "y": posicion.y
    }
    return json.dumps(obj)

@app.route('/process', methods = ['POST'])
def set_difference():
    content = request.get_json()
    diferencia.x = content['difx']
    diferencia.y = content['dify']
    return "Set difference"

@app.route('/difference', methods = ['GET'])
def get_difference():
    obj = {
        "difx": diferencia.x,
        "dify": diferencia.y
    }
    return json.dumps(obj)

if __name__ == '__main__':
    app.run()
    #app.run(debug=True, host='127.0.0.1', port=5000)