from fastapi import FastAPI
import joblib
from pathlib import Path

app = FastAPI()

# Load trained model
model = joblib.load(Path(__file__).with_name("polynomial_regression_model.pkl"))


@app.get("/")
def home():
    return {"message": "MPG Prediction API is running"}


@app.post("/predict")
def predict(horsepower: float):
    prediction = model.predict([[horsepower]])

    return {
        "horsepower": horsepower,
        "predicted_mpg": round(float(prediction[0]), 2)
    }