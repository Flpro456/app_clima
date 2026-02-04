from clima import data, lat, lon
from geocodificador import ciudad, lista
from datetime import datetime
import json

class Ciudad():
    def __init__(self, nombre, pais, latitud, longitud, historial):
        Ciudad.nombre = nombre
        Ciudad.pais = pais
        Ciudad.latitud = latitud
        Ciudad.longitud = longitud
        Ciudad.historial = historial

    def registrar_clima(temp):
        temp = data["temp"]
        fecha = datetime.now()
        Ciudad.historial.append({"temp": temp, "fecha": str(fecha)})
    
    def analizar_riesgo(self):
        if data["temp"] > 35:
            return "Alerta: Ola de calor"    
        if data["wsp"] > 50:
            return "Alerta: Vientos fuertes"
        else:
            return "Clima estable"

c1 = Ciudad(ciudad, lista["pais"], lat, lon, [])

c1.analizar_riesgo()
c1.registrar_clima()

city = {
    c1.nombre: {
        "pais": c1.pais,
        "coordenadas": [c1.latitud, c1.longitud],
        "historial": c1.historial
    }
}

try:
    with open("monitoreo_floro.json", "w") as file:
        json.dump(city, file, indent=4)
except Exception as e:
    print(e)