from flask import Blueprint, request, jsonify
import pandas as pd
import io

eda_bp = Blueprint("eda", __name__)

@eda_bp.route("/explore", methods=["POST"])
def explore_csv():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]

    try:
        df = pd.read_csv(file)

        result = {
            "shape": df.shape,
            "columns": list(df.columns),
            "dtypes": df.dtypes.astype(str).to_dict(),
            "head": df.head().to_dict(orient="records"),
            "tail": df.tail().to_dict(orient="records"),
            "describe": df.describe(include='all').fillna("").to_dict(),
            "nulls": df.isnull().sum().to_dict(),
            "unique_values": df.nunique().to_dict(),
            "memory_usage_MB": round(df.memory_usage(deep=True).sum() / 1024**2, 2),
        }

        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
