import joblib
import pandas as pd
import os
from app.schema import InputData

# Obtener la ruta absoluta del archivo actual
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, 'modelo.pkl')

# Cargar el modelo desde el archivo
model = joblib.load(model_path)

def create_input_dataframe(data: InputData):
    input_dict = {
        'area': data.area,
        'habitaciones': data.habitaciones,
        'banos': data.banos,
        'parqueaderos': data.parqueaderos,
        'estrato': data.estrato,
        'jacuzzi': data.jacuzzi,
        'chimenea': data.chimenea,
        'permite_mascotas': data.permite_mascotas,
        'gimnasio': data.gimnasio,
        'ascensor': data.ascensor,
        'conjunto_cerrado': data.conjunto_cerrado,
        'piscina': data.piscina,
        'terraza': data.terraza,
        'vigilancia': data.vigilancia,
        'antiguedad': data.antiguedad,
        'localidad': data.localidad
    }
    df_entrada = pd.DataFrame([input_dict])
    return df_entrada

def predict_price(data: InputData) -> float:
    df_entrada = create_input_dataframe(data)
    prediction = model.predict(df_entrada)
    return prediction[0]
