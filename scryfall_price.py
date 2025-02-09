import requests

def obtener_precio_carta(nombre_carta):
    url = f"https://api.scryfall.com/cards/named?exact={nombre_carta}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        nombre = data['name']
        precio_eur = data['prices']['eur']
        if precio_eur == None:
            print(f"\nNo hay precio disponible para {nombre}")
        else:
            print(f"{nombre}: {precio_eur}€")
    else:
        print(f"No se encontró la carta: {nombre_carta}")

if __name__ == "__main__":
    cartas = ["Black Lotus", "Counterspell", "Lightning Bolt"]
    for carta in cartas:
        res = obtener_precio_carta(carta)
    print() # Agregamos el salto de línea