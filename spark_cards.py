from pyspark.sql import SparkSession
import pandas as pd
import matplotlib.pyplot as plt

# 🔹 Crear la sesión de Spark
spark = SparkSession.builder \
    .appName("DecksVisualization") \
    .config("spark.sql.execution.arrow.pyspark.enabled", "true") \
    .getOrCreate()

def cargar_datos_spark(nombre_archivo):
    """Carga los datos de un archivo .ods en un DataFrame de PySpark."""
    # 📌 Leer con pandas
    df_pandas = pd.read_excel(nombre_archivo, engine="odf")

    # 🔹 Rellenar valores vacíos en la columna 'Deck'
    df_pandas["Deck"] = df_pandas["Deck"].ffill()

    # 🔹 Eliminar filas con valores nulos en 'Carta' o 'Precio'
    df_pandas = df_pandas.dropna(subset=["Carta", "Precio"])

    # 🔹 Convertir 'Precio' a tipo float
    df_pandas["Precio"] = df_pandas["Precio"].replace({'€': '', ',': '.'}, regex=True).astype(float)

    # 🔹 Convertir a DataFrame de Spark
    df_spark = spark.createDataFrame(df_pandas)
    
    return df_spark

def calcular_gasto_por_deck_spark(df_spark):
    """Calcula el gasto total por cada deck en PySpark."""
    from pyspark.sql.functions import sum as spark_sum
    
    # 🔹 Agrupar por 'Deck' y sumar precios
    gastos_spark = df_spark.groupBy("Deck").agg(spark_sum("Precio").alias("Total_Gasto"))
    
    return gastos_spark

def graficar_gastos(gastos_spark):
    """Convierte los datos a Pandas y grafica el gasto total por deck."""
    # 📌 Convertir DataFrame de Spark a Pandas
    gastos_pandas = gastos_spark.toPandas().sort_values("Total_Gasto", ascending=False)

    # 🔹 Graficar
    plt.figure(figsize=(10, 5))
    plt.barh(gastos_pandas["Deck"], gastos_pandas["Total_Gasto"], color='skyblue')
    plt.xlabel("Gasto Total (€)")
    plt.ylabel("Deck")
    plt.title("Gasto total por Deck")
    plt.gca().invert_yaxis()
    plt.show()

if __name__ == "__main__":
    archivo = "cartitas.ods"

    datos_spark = cargar_datos_spark(archivo)
    gastos_spark = calcular_gasto_por_deck_spark(datos_spark)

    # Mostrar resultados en consola y graficar
    gastos_spark.show()
    graficar_gastos(gastos_spark)
