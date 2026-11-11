
import joblib
import json
import pandas as pd

from pathlib import Path
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field


# Project paths
BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "models"
FRONTEND_DIR = BASE_DIR.parent / "frontend"


# Load model and metadata
model = joblib.load(MODEL_DIR / "car_price_model.pkl")

with open(MODEL_DIR / "metadata.json", "r") as file:
    metadata = json.load(file)


# Create FastAPI app
app = FastAPI(title="Used Vehicle Price Estimator")


# Input data structure
class CarDetails(BaseModel):
    brand: str
    model: str
    transmission: str
    year_of_manufacture: int = Field(gt=0)
    energy_capacity: int = Field(gt=0)
    kilometers_run: int = Field(ge=0)
    fuel_type: str


# Home endpoint
@app.get("/api")
def home():
    return {"message": "Used Vehicle Price Prediction API is running"}


# Metadata endpoint
@app.get("/metadata")
def get_metadata():
    return metadata


# Prediction endpoint
@app.post("/predict")
def predict_price(car: CarDetails):

    # Check whether the selected options exist
    if car.brand not in metadata["brand_models"]:
        return {"error": "Invalid brand selected"}

    if car.model not in metadata["brand_models"][car.brand]:
        return {"error": "Invalid model for the selected brand"}

    if car.transmission not in metadata["transmissions"]:
        return {"error": "Invalid transmission selected"}

    if car.fuel_type not in metadata["fuel_types"]:
        return {"error": "Invalid fuel type selected"}

    # Prepare car information
    car_data = {
        "brand": car.brand,
        "model": car.model,
        "transmission": car.transmission,
        "year_of_manufacture": car.year_of_manufacture,
        "energy_capacity": car.energy_capacity,
        "kilometers_run": car.kilometers_run
    }

    # Create fuel columns
    for fuel in metadata["fuel_types"]:
        car_data[f"fuel_{fuel}"] = (
            1 if fuel == car.fuel_type else 0
        )

    # Convert into DataFrame
    input_data = pd.DataFrame([car_data])

    # Keep the same feature order used during training
    input_data = input_data[model.feature_names_in_.tolist()]

    # Predict price
    prediction = model.predict(input_data)[0]

    return {
        "predicted_price": round(float(prediction), 2)
    }


# Serve frontend (keep this at the bottom)
app.mount(
    "/",
    StaticFiles(directory=FRONTEND_DIR, html=True),
    name="frontend"
)
