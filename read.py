import pandas as pd

def cargar_datos(nombre_archivo):
    """Carga los datos del archivo .ods y devuelve un DataFrame con las columnas necesarias."""
    df = pd.read_excel(nombre_archivo, engine="odf")
    df_filtered = df[["Carta", "Precio"]].dropna()
    df_filtered["Precio"] = df_filtered["Precio"].astype(float)
    print(df_filtered)
    return df_filtered

def calcular_suma_total(df):
    """Calcula y devuelve la suma total de los precios de todas las cartas."""
    return df["Precio"].sum()

def limite_compra(limite, precios):
    """Selecciona las cartas cuyo precio acumulado no supere el presupuesto."""
    suma = 0
    seleccionadas = []
    
    for precio in precios:
        if suma + precio <= limite:
            suma += precio
            seleccionadas.append(precio)  # Guardamos el precio
    
    return seleccionadas, suma

def filtrar_cartas_por_presupuesto(df):
    """Solicita al usuario un presupuesto y filtra las cartas que entran en ese rango."""
    presupuesto = float(input("Ingrese la cantidad máxima que está dispuesto a invertir: "))
    precios = df["Precio"].tolist()  # Convertimos la columna a lista
    seleccionados, suma_filtrada = limite_compra(presupuesto, precios)
    
    cartas_filtradas = df[df["Precio"].isin(seleccionados)]
    
    print("\nCartas dentro del presupuesto:")
    print(cartas_filtradas.to_string(index=False))
    print(f"\nSuma total de las cartas dentro del presupuesto: {suma_filtrada:.2f} €")

if __name__ == "__main__":
    archivo = "cartitas.ods"  # Nombre del archivo en la misma carpeta
    datos = cargar_datos(archivo)
    print(f"Suma total de todas las cartas: {calcular_suma_total(datos):.2f} €\n")
    filtrar_cartas_por_presupuesto(datos)
