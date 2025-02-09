import pandas as pd

def cargar_datos(nombre_archivo):
    """Carga los datos del archivo .ods y estructura los decks."""
    df = pd.read_excel(nombre_archivo, engine="odf")
    
    # Llenamos hacia adelante los valores nulos en la columna 'Deck'
    df["Deck"] = df["Deck"].ffill()
    
    # Filtramos las columnas necesarias y eliminamos filas con datos faltantes
    df_filtered = df[["Deck", "Carta", "Precio"]].dropna(subset=["Carta", "Precio"])
    
    # Limpiar y convertir los precios de texto a flotante
    df_filtered["Precio"] = df_filtered["Precio"].replace({'€': '', ',': '.'}, regex=True).astype(float)
    
    return df_filtered

def calcular_gasto_por_deck(df):
    """Calcula el gasto total por cada deck."""
    gastos = df.groupby("Deck")["Precio"].sum()
    return gastos

if __name__ == "__main__":
    archivo = "cartitas.ods"  # Asegúrate de que esté en la misma carpeta
    datos = cargar_datos(archivo)
    
    gastos_decks = calcular_gasto_por_deck(datos)
    
    print("Gasto total por cada Deck:")
    print(gastos_decks.to_string())
