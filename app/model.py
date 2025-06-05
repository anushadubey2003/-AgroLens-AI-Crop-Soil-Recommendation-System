import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'rf_model.joblib')
DATA_PATH = os.path.join(os.path.dirname(__file__), '../data/soil_crop_data.csv')

class CropRecommender:
    def __init__(self):
        self.model = joblib.load(MODEL_PATH)
        self.data = pd.read_csv(DATA_PATH)

    def predict(self, features):
        # features: dict with soil_type, pH, rainfall, temperature
        input_df = pd.DataFrame([features])
        pred = self.model.predict(input_df)[0]
        return pred

# Load once
recommender = CropRecommender()

def recommend_crop(soil_type, ph_level, rainfall, temperature):
    features = {
        'soil_type': soil_type,
        'ph': ph_level,
        'rainfall': rainfall,
        'temperature': temperature
    }
    return recommender.predict(features)
