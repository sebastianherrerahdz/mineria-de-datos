import pandas as pd
import os

# Verificar archivos en la carpeta
print("Archivos en la carpeta:")
print(os.listdir())

try:
    df = pd.read_csv("calificaciones.csv")

    # Si se carga correctamente, continuar
    df["Promedio"] = df[["Parcial1", "Parcial2", "Parcial3"]].mean(axis=1)

    promedio_general = df["Promedio"].mean()

    mejor = df.loc[df["Promedio"].idxmax()]
    peor = df.loc[df["Promedio"].idxmin()]

    aprobados = df[df["Promedio"] >= 70].shape[0]
    reprobados = df[df["Promedio"] < 70].shape[0]

    ranking = df.sort_values(by="Promedio", ascending=False)

    print("\nPromedios:")
    print(df[["Nombre", "Promedio"]])

    print("\nPromedio general:", round(promedio_general, 2))

    print("\nMejor alumno:", mejor["Nombre"], "-", round(mejor["Promedio"], 2))
    print("Peor alumno:", peor["Nombre"], "-", round(peor["Promedio"], 2))

    print("\nAprobados:", aprobados)
    print("Reprobados:", reprobados)

    print("\nRanking:")
    print(ranking[["Nombre", "Promedio"]])

except Exception as e:
    print("\n Error al leer el archivo:", e)
    print(" Asegúrate de que 'calificaciones.csv' esté en la misma carpeta")
