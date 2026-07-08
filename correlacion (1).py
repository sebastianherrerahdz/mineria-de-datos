import pandas as pd
dt = pd.read_csv("estudiantes.csv")

correlacion = dt["Asistencia"].corr(dt["Calificacion_Final"])
print("correlacion entre asistencia y calificacion final:", correlacion)

correlacion = dt["Examen"].corr(dt["Calificacion_Final"])
print("correlacion entre examen y calificacion final:", correlacion)

correlacion = dt["Horas_Estudio"].corr(dt["Calificacion_Final"])
print("correlacion entre horas de estudio y calificacion final:", correlacion)

correlacion = dt["Tareas"].corr(dt["Calificacion_Final"])
print("correlacion entre tareas y calificacion final:", correlacion)

correlacion = dt["Edad"].corr(dt["Calificacion_Final"])
print("correlacion entre edad y calificacion final:", correlacion)

