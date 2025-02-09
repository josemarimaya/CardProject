import requests

def cartas_azules_coste_3():
    # Buscar todas las cartas de color azul con coste de maná 3
    query = "color=U cmc=3"
    url = f"https://api.scryfall.com/cards/search?q={query}"
    
    while url:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            cards = data['data']
            
            for card in cards:
                print(f"- {card['name']}")
            
            # Comprobar si hay más páginas
            url = data.get('next_page', None)
        else:
            print(f"Error al buscar cartas: {response.status_code}")
            break

if __name__ == "__main__":
    cartas_azules_coste_3()

