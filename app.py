from flask import Flask, jsonify, request
from datetime import datetime
from werkzeug.routing import BaseConverter, ValidationError

app = Flask(__name__)

readings = [
    {
        'date': 10-11-2018,
        'counter': 197345367
    },
    {
        'date': 10-11-2018,
        'counter': 197345369
    }
]

@app.route('/readings', methods=['GET'])
def get_readings():
    return jsonify({'readings': readings})

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/readings', methods=['POST'])
def create_reading():
    if not request.json or not 'title' in request.json:
        abort(400)
    reading = {
        'date': request.json['date'],
        'counter': request.json.get('counter', ""),
    }
    readings.append(reading)
    return jsonify({'reading': reading}), 201