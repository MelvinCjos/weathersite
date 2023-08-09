from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json
from django.conf import settings

@csrf_exempt
def get_current_weather(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            city_name = data['city']
            output_format = data.get('output_format', 'json')

            api_key = settings.RAPIDAPI_KEY
            url = f"https://weatherapi-com.p.rapidapi.com/current.json"
            querystring = {"q": city_name}

            headers = {
                "X-RapidAPI-Key": api_key,
                "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
            }

            response = requests.get(url, headers=headers, params=querystring)
            weather_data = response.json()

            response_data = {
                "Weather": f"{weather_data['current']['temp_c']} C",
                "Latitude": weather_data['location']['lat'],
                "Longitude": weather_data['location']['lon'],
                "City": f"{city_name} India"
            }

            return JsonResponse(response_data)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request method. Use POST.'}, status=400)
