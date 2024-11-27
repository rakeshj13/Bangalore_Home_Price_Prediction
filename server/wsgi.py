from server import app
import util

if __name__ == "__main__":
    print("Starting Python Flask Server for Home Price Prediction...")
    util.load_saved_artifacts()  # Load saved artifacts before running the server
    app.run()

