import requests
import json
import os

ciudad = input("Ingresa la ciudad: ")

answer = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={ciudad}&count=1&language=es&format=json")
answer = dict(json.loads(answer.text))


list = [
    (answer)["results"][0]["latitude"],
    (answer)["results"][0]["longitude"],
    (answer)["results"][0]["country"]
]