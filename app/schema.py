from pydantic import BaseModel

class InputData(BaseModel):
    area: float
    habitaciones: int
    banos: int
    parqueaderos: int
    estrato: int
    jacuzzi: int
    chimenea: int
    permite_mascotas: int
    gimnasio: int
    ascensor: int
    conjunto_cerrado: int
    piscina: int
    terraza: int
    vigilancia: int
    antiguedad: str
    localidad: str

class PredictionResponse(BaseModel):
    price: float
