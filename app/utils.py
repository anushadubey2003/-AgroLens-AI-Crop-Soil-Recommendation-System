def get_fertilizer_suggestion(soil_type, crop):
    # Simple mock rules; expand as needed
    if soil_type == 'Loamy':
        return "Nitrogen-rich fertilizer recommended."
    elif soil_type == 'Sandy':
        return "Add organic matter and phosphate fertilizers."
    else:
        return "Balanced NPK fertilizer recommended."

def fetch_weather_forecast(location):
    # Stub for weather API call (to be implemented)
    # Could use OpenWeatherMap, WeatherAPI, etc.
    return {
        'temperature': 25,
        'rainfall': 100
    }
