import pandas as pd
import matplotlib.pyplot as plt
dt = pd.read_csv("estudiantes.csv")

correlacion = dt["Asistencia"].corr(dt["Calificacion_Final"])
print("correlacion entre asistencia y calificacion final:", correlacion)

plt.scatter(dt["Asistencia"], dt["Calificacion_Final"])
plt.xlabel("Asistencia")
plt.ylabel("Calificación final")
plt.title("Calificación final por estudiante")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

correlacion = dt["Examen"].corr(dt["Calificacion_Final"])
print("correlacion entre examen y calificacion final:", correlacion)

plt.scatter(dt["Examen"], dt["Calificacion_Final"])
plt.xlabel("Examen")
plt.ylabel("Calificación final")
plt.title("Calificación final por estudiante")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

correlacion = dt["Horas_Estudio"].corr(dt["Calificacion_Final"])
print("correlacion entre horas de estudio y calificacion final:", correlacion)

plt.scatter(dt["Horas_Estudio"], dt["Calificacion_Final"])
plt.xlabel("Horas de estudio")
plt.ylabel("Calificación final")
plt.title("Calificación final por estudiante")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

correlacion = dt["Tareas"].corr(dt["Calificacion_Final"])
print("correlacion entre tareas y calificacion final:", correlacion)

plt.scatter(dt["Tareas"], dt["Calificacion_Final"])
plt.xlabel("Tareas")
plt.ylabel("Calificación final")
plt.title("Calificación final por estudiante")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

correlacion = dt["Edad"].corr(dt["Calificacion_Final"])
print("correlacion entre edad y calificacion final:", correlacion)

plt.scatter(dt["Edad"], dt["Calificacion_Final"])
plt.xlabel("Edad")
plt.ylabel("Calificación final")
plt.title("Calificación final por estudiante")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
