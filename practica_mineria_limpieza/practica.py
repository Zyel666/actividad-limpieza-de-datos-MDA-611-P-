import pandas as pd
import numpy as np

# Cargar dataset
df = pd.read_csv("dataset_con_errores.csv")
print("Filas:", df.shape[0])
print("Columnas:", df.shape[1])
print("\nPrimeras 5 filas:")
print(df.head())

# Diagnosticar datos
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

# Copiar dataset
df_limpio = df.copy()

# Eliminar duplicados
filas_antes = len(df_limpio)
df_limpio = df_limpio.drop_duplicates()
filas_despues = len(df_limpio)
print("Duplicados eliminados:", filas_antes - filas_despues)

# Limpiar nombres
df_limpio["nombre"] = df_limpio["nombre"].astype(str).str.strip().str.title()

# Estandarizar género
df_limpio["genero"] = df_limpio["genero"].astype(str).str.strip().str.lower()
mapa_genero = {
    "m": "Masculino",
    "masculino": "Masculino",
    "f": "Femenino",
    "femenino": "Femenino"
}
df_limpio["genero"] = df_limpio["genero"].map(mapa_genero)
moda_genero = df_limpio["genero"].mode()[0]
df_limpio["genero"] = df_limpio["genero"].fillna(moda_genero)

# Estandarizar países
df_limpio["pais"] = df_limpio["pais"].astype(str).str.strip().str.lower()
mapa_paises = {
    "mexico": "México",
    "méxico": "México",
    "colombia": "Colombia",
    "argentina": "Argentina",
    "españa": "España"
}
df_limpio["pais"] = df_limpio["pais"].map(mapa_paises)

# Corregir edades
print("Edades atípicas:", ((df_limpio["edad"] < 18) | (df_limpio["edad"] > 100)).sum())
df_limpio.loc[(df_limpio["edad"] < 18) | (df_limpio["edad"] > 100), "edad"] = np.nan
mediana_edad = df_limpio["edad"].median()
df_limpio["edad"] = df_limpio["edad"].fillna(mediana_edad)
df_limpio["edad"] = df_limpio["edad"].round().astype(int)

# Limpiar ingresos
df_limpio["ingresos"] = (
    df_limpio["ingresos"]
    .astype(str)
    .str.replace("USD", "", regex=False)
    .str.replace("$", "", regex=False)
    .str.replace("€", "", regex=False)
    .str.replace(",", "", regex=False)
    .str.strip()
)
df_limpio["ingresos"] = pd.to_numeric(df_limpio["ingresos"], errors="coerce")
print("Ingresos atípicos:", ((df_limpio["ingresos"] < 0) | (df_limpio["ingresos"] > 200000)).sum())
df_limpio.loc[
    (df_limpio["ingresos"] < 0) | (df_limpio["ingresos"] > 200000),
    "ingresos"
] = np.nan
mediana_ingresos = df_limpio["ingresos"].median()
df_limpio["ingresos"] = df_limpio["ingresos"].fillna(mediana_ingresos)

# Convertir fechas
df_limpio["fecha_nacimiento"] = pd.to_datetime(
    df_limpio["fecha_nacimiento"],
    errors="coerce",
    dayfirst=True,
    format="mixed"
)

# Validar limpieza
print("\n=== DIMENSIONES FINALES ===")
print("Filas:", df_limpio.shape[0])
print("Columnas:", df_limpio.shape[1])
print("\n=== VALORES NULOS DESPUÉS DE LIMPIAR ===")
print(df_limpio.isnull().sum())
print("\n=== DUPLICADOS DESPUÉS DE LIMPIAR ===")
print(df_limpio.duplicated().sum())
print("\n=== GÉNEROS ÚNICOS ===")
print(df_limpio["genero"].value_counts())
print("\n=== PAÍSES ÚNICOS ===")
print(df_limpio["pais"].value_counts())
print("\n=== ESTADÍSTICAS DE EDAD ===")
print(df_limpio["edad"].describe())
print("\n=== ESTADÍSTICAS DE INGRESOS ===")
print(df_limpio["ingresos"].describe())

# Guardar dataset limpio
df_limpio.to_csv("dataset_limpio.csv", index=False, encoding="utf-8-sig")
print("\nArchivo guardado exitosamente: dataset_limpio.csv")
