import json

import requests

url = "https://community-open-weather-map.p.rapidapi.com/forecast"

querystring = {"q":"san francisco,us"}

headers = {
    'x-rapidapi-key': "072455c6f2msh12d73c96f3a6b7ap1c42bbjsnd29975ed71a6",
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(json.loads(response.text))