#Medidas de tendencia 
import pandas as pd
datos = pd.read_csv("estudiantes.csv")
columna = "Examen"
maximo = datos[columna].max()
minimo = datos[columna].min()
rango = maximo - minimo
varianza = datos[columna].var()
desviacion = datos[columna].std()

print("Máximo:", maximo)
print("Mínimo:", minimo)
print("Rango:", rango)
print("Varianza:", varianza)
print("Desviación estándar:", desviacion)

