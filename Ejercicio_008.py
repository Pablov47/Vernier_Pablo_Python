#Ejercicio 8
import pandas as pd

def aprobados(notas):
    
    #Convertir el diccionario a una serie de pandas.
    notas_serie = pd.Series(notas)
    #Aquí filtramos los alumnos aprobados y ordenamos las notas de mayor a menor.Y solamente se considera aprobados que una nota de 6 o superior es un aprobado, y menos de 6 es reprobado.
    aprobados = notas_serie[notas_serie >= 6].sort_values(ascending=False)
    return aprobados

notas = {'Juan':9, 'María':6.5, 'Pedro':4, 'Carmen': 8.5, 'Luis': 5}
print(aprobados(notas))

