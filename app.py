from flask import Flask, jsonify, request
from flask_restful import Resource, Api


app = Flask(__name__)

api = Api(app)

class Quotes(Resource):
    def get(self):
        return {
            'ataturk': {
                'quote': ['Yurtta sulh, cihanda sulh.', 
                    'Egemenlik verilmez, alınır.', 
                    'Hayatta en hakiki mürşit ilimdir.']
            },
            'linus': {
                'quote': ['Talk is cheap. Show me the code.']
            }

        }


api.add_resource(Quotes, '/')

if __name__ == '__main__':
    app.run(debug=True)

# readings = [
#     {
#         'date': 10-11-2018,
#         'counter': 197345367
#     },
#     {
#         'date': 10-11-2018,
#         'counter': 197345369
#     }
# ]

# @app.route('/readings', methods=['GET'])
# def get_readings():
#     return jsonify({'readings': readings})

# if __name__ == '__main__':
#     app.run(debug=True)

# @app.route('/readings', methods=['POST'])
# def create_reading():
#     if not request.json or not 'title' in request.json:
#         abort(400)
#     reading = {
#         'date': request.json['date'],
#         'counter': request.json.get('counter', ""),
#     }
#     readings.append(reading)
#     return jsonify({'reading': reading}), 201