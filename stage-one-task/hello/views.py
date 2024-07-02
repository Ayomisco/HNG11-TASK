from django.http import JsonResponse
import requests
from django.conf import settings
import logging

logger = logging.getLogger(__name__)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0].strip()
    else:
        ip = request.META.get('REMOTE_ADDR', '127.0.0.1')
    return ip


def hello(request):
    visitor_name = request.GET.get('visitor_name', 'Guest')
    client_ip = get_client_ip(request)

    if client_ip == '127.0.0.1':
        client_ip = '8.8.8.8'  # Example IP for testing

    logger.debug(f"Client IP: {client_ip}")

    location_url = f"https://ipapi.co/{client_ip}/json/"
    location_response = requests.get(location_url)
    if location_response.status_code == 200:
        location_data = location_response.json()
        city = location_data.get('city', 'Unknown')
        latitude = location_data.get('latitude')
        longitude = location_data.get('longitude')
    else:
        city = 'Unknown'
        latitude = None
        longitude = None

    logger.debug(f"Location Data: City: {city}, Latitude: {
                 latitude}, Longitude: {longitude}")

    if latitude and longitude:
        weather_url = (
            f"https://api.openweathermap.org/data/2.5/weather?"
            f"lat={latitude}&lon={longitude}&appid={
                settings.WEATHER_API_KEY}&units=metric"
        )
        weather_response = requests.get(weather_url)
        if weather_response.status_code == 200:
            weather_data = weather_response.json()
            temperature = weather_data['main']['temp']
        else:
            temperature = "Unknown"
    else:
        temperature = "Unknown"

    logger.debug(f"Temperature: {temperature}")

    greeting = f"Hello, {visitor_name}!, the temperature is {
        temperature} degrees Celsius in {city}"
    response = {
        "client_ip": client_ip,
        "location": city,
        "greeting": greeting
    }

    return JsonResponse(response)
