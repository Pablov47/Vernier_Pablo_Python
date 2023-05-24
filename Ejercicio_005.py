#crear un diccionario con los precios de las frutas.
precios = {"plátano": 1.35, "manzana": 0.80, "pera": 0.85, "naranja": 0.70}

#preguntar al usuario por una fruta y el número de kilos.Agregamos la función .lower() para que covnierta todos los caractéres en minúsculas en caso de que el usuario ingrese la fruta con alguna o todas mayúsculas.
fruta = input("Por favor, introduce una fruta: ").lower()
kilos = float(input("Por favor, introduce el número de kilos: "))

#Comprobar si la fruta está en el diccionario.
if fruta in precios:
    #Si la fruta está en el diccionario, calculamos el precio y lo mostramos.
    precio = precios[fruta] * kilos
    print("El precio de " + str(kilos) + " kilos de " + fruta + " es " + str(precio) + ".")
else:
    #Si la fruta no está en el diccionario, informamos al usuario.
    print("Lo siento, no tengo información de la fruta que has seleccionado.")
