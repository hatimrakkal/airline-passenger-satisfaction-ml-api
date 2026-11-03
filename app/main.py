import joblib
import pandas as pd
from fastapi import FastAPI
from app.schema import Observation, Prediction

app = FastAPI()

model_path = "models/airline_pipeline.joblib"
pipeline = joblib.load(model_path)

@app.post("/prediction", response_model=Prediction)
async def predict(data: Observation):

    X = pd.DataFrame([data.model_dump(by_alias=True)])

    prediction_num = pipeline.predict(X)[0]

    prediction_text = "satisfied" if prediction_num == 1 else "neutral or dissatisfied"

    return {"prediction": prediction_text}


    