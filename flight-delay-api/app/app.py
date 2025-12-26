from fastapi import FastAPI
from pydantic import BaseModel, Field
from inference_pipeline import predict
from fastapi import HTTPException

app = FastAPI(
    title="Flight Delay Prediction API",
    version="0.0.1"
)

class PredictionInput(BaseModel):
    aerolinea: str = Field(..., example="AZ")
    origen: str = Field(..., example="GIG")
    destino: str = Field(..., example="GRU")
    fecha_partida: str = Field(..., example="2025-11-10T14:30:00")
    distancia_km: float = Field(..., gt=0)

class PredictionOutput(BaseModel):
    prevision: str
    probabilidad: float


@app.post("/predict", response_model=PredictionOutput)
def predict_delay(data: PredictionInput):
    try:
        return predict(data.dict())
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
