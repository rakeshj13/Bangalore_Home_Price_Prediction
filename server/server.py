from flask import Flask, request, jsonify
import util  # Import the util.py module

app = Flask(__name__)


@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    # Ensure the artifacts are loaded when the route is accessed
    if not util.__locations:
        util.load_saved_artifacts()  # Load if not already loaded

    # Debug print to check the locations
    print(f"Locations loaded: {util.get_location_names()[:10]}...")  # Print first 10 locations for debugging

    # Return the location names as a JSON response
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)

    response = jsonify({
        'estimated_price': estimated_price
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server for Home Price Prediction...")
    util.load_saved_artifacts()  # Load saved artifacts before running the server
    app.run()




