
import joblib
import mlflow
import mlflow.sklearn

from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "backend" / "models" / "car_price_model.pkl"
METADATA_PATH = BASE_DIR / "backend" / "models" / "metadata.json"

# Load existing trained model
model = joblib.load(MODEL_PATH)

# Access the Random Forest estimator inside the pipeline
rf_model = model.named_steps["model"]

# Set experiment
mlflow.set_experiment("Used Vehicle Price Estimator")

# Start one experiment run
with mlflow.start_run(run_name="Random Forest - Final Model"):

    # 1. Log model parameters
    mlflow.log_params({
        "model_name": "Random Forest Regressor",
        "n_estimators": rf_model.n_estimators,
        "n_jobs": rf_model.n_jobs,
        "random_state": rf_model.random_state,
        "preprocessing": "StandardScaler + OneHotEncoder"
    })

    # 2. Log existing CV metrics
    mlflow.log_metrics({
        "cv_mae": 486806.770801,
        "cv_rmse": 2088016,
        "cv_r2": 0.782007
    })

    # 3. Log existing test metrics
    mlflow.log_metrics({
        "test_mae": 587108.974788,
        "test_rmse": 2960918,
        "test_r2": 0.736331
    })

    # 4. Log model and metadata files as artifacts
    mlflow.log_artifact(str(MODEL_PATH))
    mlflow.log_artifact(str(METADATA_PATH))

    print("MLflow tracking completed successfully!")

print("Experiment:", mlflow.get_experiment_by_name(
    "Used Vehicle Price Estimator"
).name)
