from geocodificador import lista
import requests
import json

lat = lista["latitud"]
lon = lista["longitud"]

def coords(lat, lon):
    answer = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true")
    answer = json.loads(answer.text)
    global data
    data = {
        "temp": answer["current_weather"]["temperature"],
        "wsp": answer["current_weather"]["windspeed"],
        "wtc": answer["current_weather"]["weathercode"]
    }
    
coords(lat, lon)