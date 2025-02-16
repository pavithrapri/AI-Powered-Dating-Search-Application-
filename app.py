from flask import Flask, render_template, request, jsonify
import json
from api_test import search_profiles  # Import function from api_test.py

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Render the homepage

@app.route('/search', methods=['POST'])
def search():
    try:
        # Ensure request has JSON data
        data = request.get_json()
        
        # Extract location from request
        location_data = data.get("location")

        # Convert string to dictionary if needed
        if isinstance(location_data, str):
            location_data = json.loads(location_data)

        # Check if location data has required keys
        if isinstance(location_data, dict) and "lat" in location_data and "lng" in location_data:
            results = search_profiles(location_data)  # Call API function
            return jsonify(results)
        else:
            return jsonify({"error": "Invalid location format"}), 400  # Bad request response

    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Internal server error

if __name__ == '__main__':
    app.run(debug=True)
