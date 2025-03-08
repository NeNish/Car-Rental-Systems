from flask import Flask, request, jsonify
import numpy as np
import pickle

app = Flask(__name__)

# Load trained model
model_path = r"C:\Users\nisha\OneDrive\Documents\N\AI biased car rental systems\data\data\models\pricing_model.pkl"
model = pickle.load(open(model_path, 'rb'))

# Expected feature names (Ensure these match the ones used during training)
FEATURE_NAMES = ["day_of_week", "hour", "demand_level", "competitor_price", "temperature", "rainfall", "traffic", "holiday", "event", "customer_rating"]

@app.route('/predict', methods=['POST'])
def predict_price():
    try:
        data = request.json  # Get JSON input
        
        # Ensure all required features are present
        missing_features = [feature for feature in FEATURE_NAMES if feature not in data]
        if missing_features:
            return jsonify({"error": f"Missing features: {missing_features}"}), 400

        # Convert input into NumPy array and ensure the features are of type float
        input_features = np.array([float(data[feature]) for feature in FEATURE_NAMES], dtype=float)
        
        # Make prediction
        price = model.predict([input_features])[0]
        
        # Convert the result to a Python float before returning it
        return jsonify({'predicted_price': float(price)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
