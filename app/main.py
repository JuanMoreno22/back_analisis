from fastapi import FastAPI
from app.model import predict_price
from app.schema import InputData, PredictionResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Lista de orígenes permitidos
origins = [
    "http://localhost",
    "http://localhost:3000",
    "https://home-prediction.vercel.app",
    # Agrega aquí otros dominios permitidos
]

# Agregar el middleware de CORS a la aplicación
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Permitir estos orígenes
    allow_credentials=True,  # Permitir el envío de cookies
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos los encabezados
)



@app.get("/")
async def root():
    return {"message": "Proyecto analisis de datos"}

@app.post("/predict", response_model=PredictionResponse)
async def predict(data: InputData):
    prediction = predict_price(data)
    return PredictionResponse(price=prediction)
