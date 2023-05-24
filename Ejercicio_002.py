#ejercicio 2
#Preguntar Nombre y Sexo
nombre = input("Por favor, introduce tu nombre: ")
sexo = input("Por favor, introduce tu sexo (M/F): ")

# Comprobar a qué grupo pertenece la persona.
if (sexo == 'F' and nombre[0] < 'M') or (sexo == 'M' and nombre[0] > 'N'):
    grupo = 'A'
else:
    grupo = 'B'

print("Perteneces al grupo " + grupo)