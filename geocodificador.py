import requests
import json
import os

ciudad = input("Ingresa la ciudad: ")

answer = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={ciudad}&count=1&language=es&format=json")
answer = dict(json.loads(answer.text))

with open("list.json", "w") as file:
    lista = [
        (answer)["results"][0]["latitude"],
        (answer)["results"][0]["longitude"],
        (answer)["results"][0]["country"]
    ]
    json.dump(lista, file, indent=2)