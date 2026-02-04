import requests
import json

ciudad = input("Ingresa la ciudad: ")

answer = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={ciudad}&count=1&language=es&format=json")
answer = dict(json.loads(answer.text))

try:
    lista = {
        "latitud": (answer)["results"][0]["latitude"],
        "longitud": (answer)["results"][0]["longitude"],
        "pais": (answer)["results"][0]["country"]
    }
except KeyError:
    print("O escribiste mal el nombre, o escribiste cualquier cosa.\nDe cualquier manera, ERROR")
