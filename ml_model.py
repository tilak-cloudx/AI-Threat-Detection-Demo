import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Train a simple model (using sample dataset)
def train_model():
    data = pd.read_csv("data/sample_dataset.csv")
    X = data.drop("label", axis=1)
    y = data["label"]

    model = RandomForestClassifier()
    model.fit(X, y)

    joblib.dump(model, "model/trained_model.pkl")

def predict_threat(features: dict):
    model = joblib.load("model/trained_model.pkl")
    df = pd.DataFrame([features])
    prediction = model.predict(df)[0]
    return prediction
