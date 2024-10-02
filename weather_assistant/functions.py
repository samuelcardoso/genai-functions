# functions.py

def get_current_weather(location, unit='celsius'):
    """
    Get the current weather for a given location.

    Args:
        location (str): The city and country code, e.g., 'New York, US'.
        unit (str): The unit for temperature, 'celsius' or 'fahrenheit'.

    Returns:
        dict: A dictionary containing weather information.
    """
    # For demonstration purposes, return dummy data.
    # In a real application, you would call a weather API like OpenWeatherMap.

    weather_info = {
        'location': location,
        'temperature': '23',
        'unit': unit,
        'description': 'Sunny',
    }
    return weather_info
