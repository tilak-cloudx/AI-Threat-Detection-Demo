import pandas as pd
import joblib

def predict_threat(features: dict):
    model = joblib.load("model/trained_model.pkl")
    df = pd.DataFrame([features])
    prediction = model.predict(df)[0]
    return prediction
