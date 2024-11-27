from flask import Flask, request, jsonify
from flask_cors import CORS
import util  # Import the util.py module

app = Flask(__name__)
CORS(app)


@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    try:
        if request.method == 'GET':
            # Extract parameters from query string
            total_sqft = float(request.args.get('total_sqft', 0))
            location = request.args.get('location', '')
            bhk = int(request.args.get('bhk', 0))
            bath = int(request.args.get('bath', 0))

            # Debugging: Log input values
            print(f"Received GET request: total_sqft={total_sqft}, location={location}, bhk={bhk}, bath={bath}")
        
        elif request.method == 'POST':
            # Extract parameters from form data
            total_sqft = float(request.form.get('total_sqft', 0))
            location = request.form.get('location', '')
            bhk = int(request.form.get('bhk', 0))
            bath = int(request.form.get('bath', 0))

            # Debugging: Log input values
            print(f"Received POST request: total_sqft={total_sqft}, location={location}, bhk={bhk}, bath={bath}")
        
        # Validate the parameters
        if not location or total_sqft <= 0 or bhk <= 0 or bath <= 0:
            raise ValueError("Invalid input parameters")

        # Call utility function to get estimated price
        estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)

        # Build and return response
        response = jsonify({
            'estimated_price': estimated_price
        })
    except Exception as e:
        print(f"Error while predicting price: {e}")
        response = jsonify({'error': str(e)})

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response



@app.route('/predict_home_price', methods=['GET','POST'])
def predict_home_price():
    try:
        # Parse input parameters
        total_sqft = float(request.args.get('total_sqft', 0))
        location = request.args.get('location', '')
        bhk = int(request.args.get('bhk', 0))
        bath = int(request.args.get('bath', 0))

        # Validate input
        if not location or total_sqft <= 0 or bhk <= 0 or bath <= 0:
            raise ValueError("Invalid input parameters")

        # Call utility function to get estimated price
        estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)

        # Build response
        response = jsonify({
            'estimated_price': estimated_price
        })
    except Exception as e:
        print(f"Error while predicting price: {e}")
        response = jsonify({'error': str(e)})

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print("Starting Python Flask Server for Home Price Prediction...")
    util.load_saved_artifacts()  # Load saved artifacts before running the server
    app.run(port=5000)  # Ensure port is set explicitly
