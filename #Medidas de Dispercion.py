#Medidas de Dispercion
import pandas as pd

datos = pd.read_csv("estudiantes.csv")

columnas = ["Edad", "Asistencia", "Tareas", "Examen", "Calificacion_Final", "Horas_Estudio"]

for columna in columnas:

    maximo = datos[columna].max()
    minimo = datos[columna].min()
    rango = maximo - minimo
    varianza = datos[columna].var()
    desviacion = datos[columna].std()

    print("\nVariable:", columna)
    print("Máximo:", maximo)
    print("Mínimo:", minimo)
    print("Rango:", rango)
    print("Varianza:", varianza)
    print("Desviación estándar:", desviacion)