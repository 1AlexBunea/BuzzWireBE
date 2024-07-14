# your_app/views.py
from django.http import JsonResponse
from rest_framework.decorators import api_view
import requests
from urllib.parse import unquote
from decouple import config

api_key = config('api_key')

@api_view(['GET'])
def get_data(request, encoded_sentence):
    # Decode the URL-encoded sentence
    print("get request")

    decoded_sentence = unquote(encoded_sentence)
    
    print(f'Received request with decoded sentence: {decoded_sentence}')
    
    url = f'https://newsapi.org/v2/everything?q={decoded_sentence}&sortBy=popularity&apiKey={api_key}'
    
    # Replace this with your actual database API call
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        api_response = response.json()
        return JsonResponse(api_response)
    except requests.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)
