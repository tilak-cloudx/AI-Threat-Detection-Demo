import os
import pandas as pd
import joblib

# Load model once at startup
model_path = os.path.join(os.path.dirname(__file__), "model", "trained_model.pkl")
model = joblib.load(model_path)

def predict_threat(features: dict):
    """
    Predict threat level from features dict
    """
    df = pd.DataFrame([features])
    prediction = model.predict(df)[0]
    return prediction
