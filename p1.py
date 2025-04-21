rules = [
 {"weather": "sunny", "recommendation": "Take a bicycle."},
 {"weather": "rainy", "recommendation": "Take an umbrella."},
 {"weather": "snowy", "recommendation": "Take skis or snowboard."},
 {"weather": "windy", "recommendation": "Take a kite."},
 {"weather": "foggy", "recommendation": "Be careful and consider delaying travel."},
 {"weather": "cloudy", "recommendation": "Consider walking."},
 {"weather": "stormy", "recommendation": "Stay indoors and wait for the storm to pass."}
]
def recommend_transportation(weather):
    for rule in rules:
        if rule["weather"] == weather:
            return rule["recommendation"]
    return "No recommendation available for this weather."
# Example usage:
weather_today = "rainy"
recommendation = recommend_transportation(weather_today)
print(f"For weather '{weather_today}', recommendation: {recommendation}")