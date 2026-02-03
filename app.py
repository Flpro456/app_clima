from clima import data, lat, lon
from geocodificador import ciudad, lista
from datetime import datetime

class Ciudad():
    nombre = ciudad
    pais = lista["pais"]
    latitud = lat
    longitud = lon
    historial = []

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

c1 = Ciudad()

c1.analizar_riesgo()