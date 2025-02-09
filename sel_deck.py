from pay_4_deck import cargar_datos

def mostrar_detalles_deck(df):
    """Permite al usuario seleccionar un deck y muestra su gasto total y cartas."""
    decks_disponibles = df["Deck"].unique()
    
    while True:
        print("\nDecks disponibles:")
        for idx, deck in enumerate(decks_disponibles, start=1):
            print(f"{idx}. {deck}")
        
        seleccion = input("\nSeleccione el número del deck que desea ver (o 'q' para salir): ")
        
        if seleccion.lower() == 'q':
            print("Saliendo...")
            break
        
        if seleccion.isdigit():
            seleccion = int(seleccion) - 1
            if 0 <= seleccion < len(decks_disponibles):
                deck_seleccionado = decks_disponibles[seleccion]
                cartas_deck = df[df["Deck"] == deck_seleccionado]
                gasto_total = cartas_deck["Precio"].sum()
                
                print(f"\nCartas del deck '{deck_seleccionado}':\n")
                print(cartas_deck[["Carta", "Precio"]].to_string(index=False))
                print(f"\nGasto total para el deck '{deck_seleccionado}': {gasto_total:.2f} €")

                continuar = input("\n¿Desea consultar otro deck? (y/n): ")
                if continuar.lower() != 'y':
                    print("\nGracias por usar nuestros servicios. Hasta la próxima\n")
                    break
            else:
                print("\nIntroduzca un valor válido para los decks disponibles.")
        else:
            print("Entrada inválida. Por favor, introduce un número o 'q' para salir.")

if __name__ == "__main__":
    archivo = "cartitas.ods"  # Asegúrate de que el archivo esté en la misma carpeta
    datos = cargar_datos(archivo)
    
    mostrar_detalles_deck(datos)