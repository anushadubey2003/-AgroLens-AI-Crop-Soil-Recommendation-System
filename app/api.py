from .model import recommend_crop as rc
from .utils import get_fertilizer_suggestion

def recommend_crop(soil_type, ph_level, rainfall, temperature):
    return rc(soil_type, ph_level, rainfall, temperature)

def get_fertilizer_suggestion(soil_type, crop):
    return get_fertilizer_suggestion(soil_type, crop)
