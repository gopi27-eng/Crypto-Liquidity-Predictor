import os
import joblib
import pandas as pd
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['DEBUG'] = True

# Define the paths to the model and encoder
MODEL_PATH = 'models/Randomforest_Regression_model.pkl'
ENCODER_PATH = 'models/TargetEncoder.pkl'

# Load the model and encoder
try:
    print("Attempting to load model and encoder...")
    with open(MODEL_PATH, 'rb') as f:
        model = joblib.load(f)
    print("Model loaded successfully.")
    with open(ENCODER_PATH, 'rb') as f:
        encoder = joblib.load(f)
    print("Encoder loaded successfully.")

except FileNotFoundError as e:
    print(f"Error loading files: {e}")
    model = None
    encoder = None

@app.route('/')
def home():
    if model and encoder:
        return "The Cryptocurrency Prediction API is running!"
    else:
        return "Model or encoder not loaded. Please check the server logs."

@app.route('/predict', methods=['POST'])
def predict():
    if not model or not encoder:
        return jsonify({'error': 'Model or encoder not loaded'}), 500

    try:
        data = request.get_json(silent=True)
        if data is None:
            data = request.form.to_dict()

        required_fields = ['Symbol', 'Price', '1h Price Change', '24h Price Change', '7d Price Change', '24h Volume', 'Market Cap']
        
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f"Missing input data for: {field}"}), 400

        input_features = {
            'Symbol': data['Symbol'],
            '1h': float(data['1h Price Change']),
            '24h': float(data['24h Price Change']),
            '7d': float(data['7d Price Change']),
            'log_price': np.log1p(float(data['Price'])),
            'log_24h_volume': np.log1p(float(data['24h Volume'])),
            'log_mkt_cap': np.log1p(float(data['Market Cap'])),
        }
        
        input_df = pd.DataFrame([input_features])

        # Renaming the 'Symbol' column to 'symbol' to match what the encoder expects.
        input_df = input_df.rename(columns={'Symbol': 'symbol'})

        # The encoder now finds the 'symbol' column correctly
        input_df['encoded_symbol'] = encoder.transform(input_df[['symbol']])
        input_df = input_df.drop('symbol', axis=1)

        final_features = ['log_price', '1h', '24h', '7d', 'log_24h_volume', 'log_mkt_cap', 'encoded_symbol']
        input_df = input_df[final_features]

        prediction = model.predict(input_df)[0]

        return jsonify({'prediction': float(prediction)})

    except Exception as e:
        print(f"Prediction Error: {e}")
        return jsonify({'error': f"An error occurred during prediction: {e}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
