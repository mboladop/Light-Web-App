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



