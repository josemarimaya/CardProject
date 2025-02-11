import pandas as pd
import requests
from collections import defaultdict

url_base = "https://api.scryfall.com/cards/named?exact="

def cargar_datos(nombre_archivo):
    df = pd.read_excel(nombre_archivo, engine="odf")
    return df["Carta"].dropna()

def obtener_color_identidad(nombre_carta):
    url = f"{url_base}{nombre_carta}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if "color_identity" in data:
            # Convertimos la lista de colores en una cadena separada por comas (ej. 'U,R')
            return ",".join(data["color_identity"])
        else:
            return ""
    else:
        print(f"No se encontró la carta: {nombre_carta}")
        return ""

def agrupar_cartas_por_color(lista_cartas):
    colores_dict = defaultdict(list)
    
    for carta in lista_cartas:
        colores = obtener_color_identidad(carta)
        colores_dict[colores].append(carta)
    
    return colores_dict

if __name__ == "__main__":
    datos = cargar_datos("cartitas.ods").tolist()
    colores_cartas = agrupar_cartas_por_color(datos)

    # Imprimir el diccionario con los colores como claves y cartas como valores
    for colores, cartas in colores_cartas.items():
        color_display = colores if colores else "Incoloras"
        print(f"{color_display}: {cartas}")
