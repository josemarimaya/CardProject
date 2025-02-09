import pandas as pd
import requests

url_base = f"https://api.scryfall.com/cards/named?exact="

def cargar_datos(nombre_archivo):

    df = pd.read_excel(nombre_archivo, engine="odf")
    df_filtered = df["Carta"].dropna()
    return df_filtered

def obtener_precio_carta(nombre_carta):
    url = f"{url_base}{nombre_carta}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        nombre = data['name']
        if nombre == nombre_carta:
            precio_eur = data['prices']['eur']
            if precio_eur is None:
                return f"No hay precio disponible para {nombre}"
            else:
                return f"{nombre}: {precio_eur}€"
    else:
        f"No se encontró la carta: {nombre_carta}"

def sumatorio_total(datos):
    res = 0
    for carta in datos:
        url = f"{url_base}{carta}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if "name" in data:  # Aseguramos que la clave 'name' esté presente
                nombre = data['name']
                if nombre == carta:
                    precio_eur = data['prices']['eur']
                    if precio_eur is not None:
                        precio = float(precio_eur)
                        res += precio
        else:
            print(f"No se encontró: {carta}")
    
    return res
        


if __name__ == "__main__":
    datos = cargar_datos("cartitas.ods").tolist()

    for carta in datos:
        res = obtener_precio_carta(carta)
        print(f"{res}")

    total = sumatorio_total(datos)
    print(f"\nSuma total de todas las cartas: {total}€")