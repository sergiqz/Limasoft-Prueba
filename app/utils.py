# app/utils.py

import os
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# Configura la conexión a la base de datos con SQLAlchemy
engine = create_engine('mysql+mysqlconnector://root:sergio1997@localhost/limasoftbd')

# Función para obtener los datos
def obtener_datos():
    query = "SELECT * FROM empleados"
    df = pd.read_sql(query, engine)
    return df

# Asegurarse de que el directorio 'static/images' exista
def crear_directorio_estatico():
    if not os.path.exists('app/static/images'):
        os.makedirs('app/static/images')

# Función para crear los gráficos y guardarlos en la carpeta /static/images
def crear_graficos(df):
    crear_directorio_estatico()

    # Gráfico de barras para la relación Edad vs Salario
    plt.figure(figsize=(10,6))
    plt.bar(df['edad'], df['salario'], color='skyblue')
    plt.title('Relación entre Edad y Salario', fontsize=16)
    plt.xlabel('Edad', fontsize=14)
    plt.ylabel('Salario (S/.)', fontsize=14)
    plt.savefig('app/static/images/edad_vs_salario.png')
    plt.close()

    # Gráfico circular: Cantidad de personas por ciudad
    ciudad_counts = df['ciudad'].value_counts()
    plt.figure(figsize=(8,8))
    plt.pie(ciudad_counts, labels=ciudad_counts.index, autopct='%1.1f%%', startangle=140,
            colors=['lightcoral', 'lightskyblue', 'lightgreen', 'gold', 'pink'])
    plt.title('Cantidad de Personas por Ciudad', fontsize=16)
    plt.savefig('app/static/images/personas_por_ciudad.png')
    plt.close()
