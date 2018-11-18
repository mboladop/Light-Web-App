from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from flask_restful import Resource, Api, reqparse 
import datetime
from flask_cors import cross_origin
import dateutil.parser, datetime
from bson.json_util import dumps
import os

app = Flask(__name__)



@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

app.config['MONGO_DBNAME'] = os.environ.get("MONGODB_NAME")
app.config['MONGO_URI'] = os.environ.get("MONGODB_URI")


mongo = PyMongo(app)

@app.route('/getreadings/<year>/<month>', methods=['GET'])
@cross_origin()
def get_readings(year, month)
    resultados = dumps(mongo.db.readings.aggregate([
     {
       "$project":
         {
           "counter": "$counter",
           "date": "$date",
           "year": { "$year": "$date" },
           "month": { "$month": "$date" }
           }
     },
     { "$match" : {  "year": int(year) , "month" : int(month)} }
   ]
     ))
    return resultados

# def get_readings_month():
#     now = datetime.datetime.now()
#     year = now.year
#     month = now.month
#     yesterday = now.day - 1
#     dateStr = str(year) + "-" + str(month) + "-" + str(yesterday)
#     date = dateutil.parser.parse(dateStr)
#     resultados = dumps(mongo.db.readings.find({'date' : { '$gt' : date}},{'date':'1'}))
#     return resultados

@app.route('/addreadings', methods=['POST'])
def add_readings():
    content = request.values.get('counter')
    reading = {
        "date" : datetime.datetime.utcnow(),
        "counter": content
        }

    insert_reading = mongo.db.readings.insert_one(reading)
    return 'reading inserted'


api = Api(app)

parser = reqparse.RequestParser()


class readings(Resource):

    # get method
    def get(self):
        return {
            
                'id1': {'datetime': 10-11-2018,
                'counter': 197345367}
            ,
            
                'id2': {'datetime': 10-11-2018,
                'counter': 197345369}
        }
    #post method
    def post(self):
        parser.add_argument('quote', type=str)
        args = parser.parse_args()

        return {
            'status': True,
            'quote': '{} added. Good'.format(args['quote'])
        }

api.add_resource(readings, '/')


if __name__ == '__main__':
    app.run(debug=True)



# parser = reqparse.RequestParser()
# def post(self):
#         parser.add_argument('quote', type=str)
#         args = parser.parse_args()

#         return {
#             'status': True,
#             'quote': '{} added. Good'.format(args['quote'])
#         }

# class Quotes(Resource):
#     def get(self):
#         return {
#             'ataturk': {
#                 'quote': ['Yurtta sulh, cihanda sulh.', 
#                     'Egemenlik verilmez, alınır.', 
#                     'Hayatta en hakiki mürşit ilimdir.']
#             },
#             'linus': {
#                 'quote': ['Talk is cheap. Show me the code.']
#             }

#         }


# api.add_resource(Quotes, '/')

# if __name__ == '__main__':
#     app.run(debug=True)

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