nombre_archivo = "cartitas.ods"
from load_data import cargar_datos
from filters import limite_compra, calcular_suma_total

def gasto_minimo(datos):

    presupuesto = float(input("Ingrese la cantidad máxima que está dispuesto a invertir: "))
 
    precios = sorted(datos["Precio"].tolist()) # Convertimos la columna a lista y ordenamos

    seleccionados, suma_filtrada = limite_compra(presupuesto, precios)
    cartas_filtradas = datos[datos["Precio"].isin(seleccionados)]
    
    print("\nCartas dentro del presupuesto:")
    print(cartas_filtradas.to_string(index=False))
    print(f"\nSuma total de las cartas dentro del presupuesto: {suma_filtrada:.2f} €")
    print(f"Cartas en total: {len(cartas_filtradas)}")

if __name__ == "__main__":
    
    datos = cargar_datos(nombre_archivo)
    print(f"\nSuma total del precio de todas las cartas necesarias: {calcular_suma_total(datos):.2f} €\n")
    gasto_minimo(datos)
    