from position import Position
from flask import request
from flask import Flask
import json

app = Flask(__name__)
posicion = Position()

@app.route('/', methods = ['GET', 'POST'])
def api_root():
    return 'Position service'

@app.route('/service', methods = ['POST'])
def set_position():
    content = request.get_json()
    posicion.x = content['x']
    posicion.y = content['y']
    return "Set position"

@app.route('/position', methods = ['GET'])
def get_position():
    obj = {
        "x": posicion.x,
        "y": posicion.y
    }
    return json.dumps(obj)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)