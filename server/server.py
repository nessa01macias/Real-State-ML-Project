from flask import Flask, request, jsonify
app = Flask(__name__)
from utils import get_location_names, get_estimation


# Returns all the locations posibilities.
@app.route('/get_locations')
def get_locations():
    response = jsonify({
        'locations': get_location_names()
    }) 
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# Returns the prediction from the house.
@app.route('/predict_price', methods=['POST'])
def predict_price():
    try: 
        total_sqft = request.form['total_sqft']
        location = request.form['location']
        bhk = int(request.form['bhk'])
        bath = int(request.form['bath'])

        response = jsonify({
        'estimated_price': get_estimation(total_sqft, bath, bhk, location)
        })
    except:
        response = { 'estimated_price': 'ERROR'}
        
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting the server for Home Price Prediction...")
    app.run()