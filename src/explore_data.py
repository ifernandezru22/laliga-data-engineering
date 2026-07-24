# a1. Importar pandas
import pandas as pd


# a2. Leer data/LaLiga_Matches.csv
df = pd.read_csv('data/LaLiga_Matches.csv')

# a3. Mostrar las primeras 10 filas
#print("10 primeras filas de dataframe LaLiga:\n")
#print(f"{df.head(10)}\n")

# a4. Mostrar cuántas filas y columnas tiene
#print(f"Filas: {df.shape[0]}, Columnas: {df.shape[1]}\n") 

# a5. Mostrar los nombres de las columnas
#print(f"Columnas: {df.columns.tolist()}\n")

# a6. Mostrar el tipo de dato inferido para cada columna.
#df.dtypes

# b1. Valores nulos

nulos_columnas = df.isnull().sum()
print(nulos_columnas)

# b2. Filas duplicadas

num_filasDuplicadas = df.duplicated().sum()
print(f"Filas duplicadas: {num_filasDuplicadas}")

# b3. Valores distintos en FTR y HTR

print(df["FTR"].unique())
print(df["HTR"].unique())

# b4. Rango de fechas cubiertas en el csv

dates = pd.to_datetime(df["Date"], format="%d-%m-%Y")
print(dates.min())
print(dates.max())

# c1. Verificación nulos y coherencia de datos

filas_nulas = df[df.isnull().any(axis=1)]

df.groupby("Season").size() # Última temporada incompleta
df[(df["FTHG"] > df["FTAG"]) & (df["FTR"] != "H")]
