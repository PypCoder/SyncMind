from flask import Blueprint, request, jsonify
import joblib
import pandas as pd
import os

house_model_bp = Blueprint("model", __name__)

# Load model only once at startup
model_path = os.path.join(os.path.dirname(__file__), "models/house_price_model.pkl")

try:
    model = joblib.load(model_path)
except Exception as e:
    print(f"❌ Error loading model: {e}")
    model = None  # Fallback to prevent crash

@house_model_bp.route("/predicthouseprice", methods=["POST"])
def predict_price():
    try:
        input_data = request.json

        # Check if model loaded
        if model is None:
            return jsonify({"error": "Model not loaded"}), 500

        # Convert to DataFrame
        df = pd.DataFrame([input_data])

        # Predict
        price = float(model.predict(df)[0])

        return jsonify({"predicted_price": price})

    except Exception as e:
        print(f"❌ Exception during prediction: {e}")
        return jsonify({"error": str(e)}), 500
