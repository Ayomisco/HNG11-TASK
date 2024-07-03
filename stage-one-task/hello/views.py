from django.http import JsonResponse
import requests
from django.conf import settings
import logging

''' Added adequate comments to help guide the Mentors
  or any brogrammers or sisgrammer going through my code '''

# Prepare the logger - because every hero needs a sidekick to keep track of things!
logger = logging.getLogger(__name__)


def get_client_ip(request):
    # Try to get the IP address from the HTTP_X_FORWARDED_FOR header (if your request has been forwarded by a proxy)
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        # If there's a list of IPs, grab the first one and trim any extra spaces
        ip = x_forwarded_for.split(',')[0].strip()
    else:
        # If no proxy is involved, grab the IP address directly from the remote address
        # Fall back to localhost if all else fails
        ip = request.META.get('REMOTE_ADDR', '127.0.0.1')
    return ip


def hello(request):
    # Greet the visitor; use 'Guest' if they didn’t bother to introduce themselves
    visitor_name = request.GET.get('visitor_name', 'Guest')
    # Get the client IP address - this might reveal more than their browsing history
    client_ip = get_client_ip(request)

    # If we’re running locally, let’s pretend to be Google DNS for some globe-trotting fun
    if client_ip == '127.0.0.1':
        client_ip = '8.8.8.8'  # Just a little white lie for testing purposes

    logger.debug(f"Client IP: {client_ip}")  # Log the IP like a nosy neighbor

    # Prepare to stalk the location using the client IP
    location_url = f"https://ipapi.co/{client_ip}/json/"
    location_response = requests.get(location_url)
    if location_response.status_code == 200:
        # Successfully located them! (Big Brother is impressed)
        location_data = location_response.json()
        city = location_data.get('city', 'Unknown')
        latitude = location_data.get('latitude')
        longitude = location_data.get('longitude')
    else:
        # Failed to locate them; guess we'll need better tracking next time
        city = 'Unknown'
        latitude = None
        longitude = None

    logger.debug(f"Location Data: City: {city}, Latitude: {
                 latitude}, Longitude: {longitude}")

    # Only check the weather if we know where in the world the person is
    if latitude and longitude:
        # Fetch the weather like a true meteorologist (minus the green screen)
        weather_url = (
            f"https://api.openweathermap.org/data/2.5/weather?"
            f"lat={latitude}&lon={longitude}&appid={
                settings.WEATHER_API_KEY}&units=metric"
        )
        weather_response = requests.get(weather_url)
        if weather_response.status_code == 200:
            # Weather report obtained! Mother Nature approves.
            weather_data = weather_response.json()
            temperature = weather_data['main']['temp']
        else:
            # Could not fetch the weather - someone's clouded our sunshine
            temperature = "Unknown"
    else:
        temperature = "Unknown"

    # Log the temperature like a wannabe weather app
    logger.debug(f"Temperature: {temperature}")

    # Prepare a warm greeting, temperature included, because we’re friendly like that
    greeting = f"Hello, {visitor_name}! The temperature is {
        temperature} degrees Celsius in {city}"
    response = {
        "client_ip": client_ip,
        "location": city,
        "greeting": greeting
    }

    # Return the JsonResponse, fully baked and ready to serve!
    return JsonResponse(response)
