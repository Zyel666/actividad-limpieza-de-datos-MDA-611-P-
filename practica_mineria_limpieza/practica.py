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
