from flask import Flask, request, jsonify
app = Flask(__name__)
import utils



@app.route('/get_locations')
def get_locations():
    return utils.get_location_names()



if __name__ == "__main__":
    print("Starting the server for Home Price Prediction...")
    app.run()