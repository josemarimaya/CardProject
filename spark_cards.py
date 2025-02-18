from pyspark.sql import SparkSession
import pandas as pd
import matplotlib.pyplot as plt

# Iniciar una sesión de Spark
spark = SparkSession.builder.appName("DecksVisualization").getOrCreate()

def cargar_datos_spark(nombre_archivo):
    """Carga los datos en un DataFrame de PySpark."""
    df_pandas = pd.read_excel(nombre_archivo, engine="odf")
    
    # Corregir el método de relleno de NaN en "Deck"
    df_pandas["Deck"] = df_pandas["Deck"].ffill()
    
    df_pandas = df_pandas.dropna(subset=["Carta", "Precio"])  # Eliminar filas con valores nulos en 'Carta' o 'Precio'
    
    # Convertir precios a float
    df_pandas["Precio"] = df_pandas["Precio"].replace({'€': '', ',': '.'}, regex=True).astype(float)
    
    # Convertir a un DataFrame de Spark
    df_spark = spark.createDataFrame(df_pandas)
    return df_spark

def calcular_gasto_por_deck_spark(df_spark):
    """Calcula el gasto total por cada deck usando PySpark."""
    gastos_spark = df_spark.groupBy("Deck").sum("Precio")
    return gastos_spark

def graficar_gastos(gastos_spark):
    """Convierte los datos a Pandas y grafica el gasto total por deck."""
    gastos_pandas = gastos_spark.toPandas()
    gastos_pandas = gastos_pandas.sort_values("sum(Precio)", ascending=False)  # Ordenar por gasto
    
    # Graficar
    plt.figure(figsize=(10, 5))
    plt.barh(gastos_pandas["Deck"], gastos_pandas["sum(Precio)"], color='skyblue')
    plt.xlabel("Gasto Total (€)")
    plt.ylabel("Deck")
    plt.title("Gasto total por Deck")
    plt.gca().invert_yaxis()  # Para que el deck con más gasto aparezca arriba
    plt.show()

if __name__ == "__main__":
    archivo = "cartitas.ods"
    
    datos_spark = cargar_datos_spark(archivo)
    gastos_spark = calcular_gasto_por_deck_spark(datos_spark)
    
    graficar_gastos(gastos_spark)
