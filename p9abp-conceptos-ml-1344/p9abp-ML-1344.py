
# Luis Adrian Hinojos Chavez
# Practica 9 - Reto ABP
# Numero de lista: 29

import pandas as pd

print("RETO ABP: ANALISIS DE ENTREGAS")
print("Adrian Hinojos NC 1344")
print("Version de Pandas:", pd.__version__)
print("Numero de lista: 29")

# Dataset correspondiente al numero de lista 29
datos29 = {
    "distancia_km": [3.8, 2.0, 4.4, 1.9, 6.0],
    "trafico_nivel": [3, 1, 2, 3, 2],
    "edad_repartidor": [39, 28, 31, 45, 23],
    "tiempo_entrega_min": [36, 14, 33, 20, 52]
}

df = pd.DataFrame(datos29)

# Clasificar el tiempo de entrega
def clasificar_tiempo(tiempo):
    if tiempo <= 20:
        return "Rapida"
    elif tiempo <= 35:
        return "Normal"
    else:
        return "Lenta"

df["clasificacion"] = df["tiempo_entrega_min"].apply(
    clasificar_tiempo
)

print("\nAnalisis de las entregas:")
print(df)

print("\nCantidad de entregas por clasificacion:")
print(df["clasificacion"].value_counts())

print("\nPromedio de tiempo de entrega:")
print(round(df["tiempo_entrega_min"].mean(), 2), "minutos")

print("\nPromedio de tiempo segun el trafico:")
print(df.groupby("trafico_nivel")["tiempo_entrega_min"].mean())

# Guardar resultados
df.to_csv("resultado_abp29.csv", index=False)

print("\nResultados guardados en resultado_abp29.csv")
print("Programa realizado por Adrian Hinojos NC 1344")