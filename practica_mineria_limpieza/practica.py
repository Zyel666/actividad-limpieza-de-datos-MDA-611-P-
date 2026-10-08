import pandas as pd
import numpy as np

# Cargar el dataset
df = pd.read_csv("dataset_con_errores.csv")

# Ver dimensiones
print("Filas:", df.shape[0])
print("Columnas:", df.shape[1])

# Ver primeras filas
print("\nPrimeras 5 filas:")
print(df.head())


# ---------------------------------------------------
# DIAGNÓSTICO DEL DATASET
# ---------------------------------------------------
print("\n=== INFORMACIÓN GENERAL ===")
print(df.info())
print("\n=== VALORES NULOS ===")
print(df.isnull().sum())
print("\n=== FILAS DUPLICADAS ===")
print("Cantidad:", df.duplicated().sum())
print("\n=== ESTADÍSTICAS DE EDAD ===")
print(df["edad"].describe())
print("\n=== VALORES ÚNICOS DE GÉNERO ===")
print(df["genero"].value_counts(dropna=False))
print("\n=== VALORES ÚNICOS DE PAÍS ===")
print(df["pais"].value_counts(dropna=False))

print("\n=== VALORES NULOS INICIALES ===")
    nulos_iniciales = df.isnull().sum()
    print(nulos_iniciales.to_string())
    print(f"Total de valores nulos: {int(nulos_iniciales.sum())}")

    duplicados_iniciales = int(df.duplicated().sum())
    print("\n=== FILAS DUPLICADAS ===")
    print(f"Cantidad: {duplicados_iniciales}")

    edades_invalidas_iniciales = int(((df["edad"] < 18) | (df["edad"] > 100)).sum())
    print("\n=== EDADES FUERA DEL RANGO 18 A 100 ===")
    print(f"Cantidad: {edades_invalidas_iniciales}")

    print("\n=== VALORES ÚNICOS DE GÉNERO ===")
    print(df["genero"].value_counts(dropna=False).to_string())

    print("\n=== VALORES ÚNICOS DE PAÍS ===")
    print(df["pais"].value_counts(dropna=False).to_string())