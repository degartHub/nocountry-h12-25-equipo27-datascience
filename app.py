
# ============================================================
# 2. Importación de las librerias necesarias
# ============================================================

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

import joblib
import pandas as pd
from datetime import datetime
import time

# ============================================================
# 3. METADATOS de la app
# ============================================================

app = FastAPI(
    title="Flight Delay Predictor API",
    version="0.1", #Versión de prueba para BackEnd y MVP 
    description="Microservicio de predicción de retrasos de vuelos"
)

# ============================================================
# 4. Carga del PIPELINE
# ============================================================

try:
    pipeline = joblib.load("flight_delay_inference_pipeline.joblib")
except Exception as e:
    raise RuntimeError(f"Error cargando el pipeline: {e}")

# ============================================================
# 5. Definición del contrato en la API
# ============================================================

class FlightRequest(BaseModel):
    aerolinea: str
    origen: str
    destino: str
    fecha_partida: str
    distancia_km: float

# ============================================================
# 6. Función de transformación de datos para el Modelo
# ============================================================

def parse_request_to_dataframe(request: FlightRequest) -> pd.DataFrame:
    try:
        dt = datetime.fromisoformat(request.fecha_partida)
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail="fecha_partida debe estar en formato ISO: YYYY-MM-DDTHH:MM:SS"
        )

    data = {
        "aerolinea": request.aerolinea,
        "origen": request.origen,
        "destino": request.destino,
        "dia_semana": dt.strftime("%A"),
        "hora_salida": dt.hour,
        "distancia_km": request.distancia_km
    }

    return pd.DataFrame([data])

# ============================================================
# 7. Definición del ENDPOINT /predict
# ============================================================

@app.post("/predict")
def predict_flight_delay(request: FlightRequest):
    start_time = time.time()

    df = parse_request_to_dataframe(request)

    proba = pipeline.predict_proba(df)[0][1]
    prediction = "Retrasado" if proba >= 0.5 else "Puntual"

    latency_ms = (time.time() - start_time) * 1000

    return {
        "prevision": prediction,
        "probabilidad": round(proba, 3),
        "latencia_ms": round(latency_ms, 2)
    }
