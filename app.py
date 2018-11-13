from flask import Flask, jsonify, abort



app = Flask(__name__)

readings = [
    {
        'date': 12-10-2018,
        'counter': 197345367
    },
    {
        'date': 13-10-2018,
        'counter': 197345369
    }
]

@app.route('/readings', methods=['GET'])
def get_readings():
    return jsonify({'readings': readings})

if __name__ == '__main__':
    app.run(debug=True)