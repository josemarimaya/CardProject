import pandas as pd

def cargar_datos(nombre_archivo):
    """Carga los datos del archivo .ods y devuelve un DataFrame con las columnas necesarias."""
    df = pd.read_excel(nombre_archivo, engine="odf")
    df_filtered = df[["Carta", "Precio"]].dropna()
    df_filtered["Precio"] = df_filtered["Precio"].astype(float)
    print(df_filtered)
    return df_filtered

cargar_datos("cartitas.ods")