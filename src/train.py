import os
import joblib
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from src.data import load_data, Preprocessor


ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "data" / "airline_passenger_satisfaction.csv"

data = load_data(DATA_PATH)

data.dropna(inplace=True)

X = data.drop(columns=["satisfaction"])
y = data["satisfaction"].map({"satisfied": 1, "neutral or dissatisfied": 0})

pipeline = Pipeline([
    ("preprocessor", Preprocessor()),
    ("scaler", StandardScaler()),
    ("classifier", LogisticRegression(max_iter=1000, random_state=42))
])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

pipeline.fit(X_train, y_train)

os.makedirs("models", exist_ok=True)

joblib.dump(pipeline, "models/airline_pipeline.joblib")