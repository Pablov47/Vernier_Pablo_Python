
name=input ('¿Cuál es tu nombre?')
papellido=input('¿Cuál es tu primer apellido?')
sapellido=input('¿Cuál es tu segundo apellido?')
año_nacimiento= int(input('¿En qué año naciste?'))
mes_día=input('¿En qué mes y día naciste? (en el siguiente formato “mm-dd”)')
año_actual=2022

nombre_completo = name + " " + papellido + " " + sapellido
nombre_completo_mayus = nombre_completo.upper()
print(f"Este es tu nombre completo en mayúsculas {nombre_completo_mayus}.")
nombre_completo_minus = nombre_completo.lower()
print(f'Este es tu nombre completo en minúsculas {nombre_completo_minus}.')
fecha_nacimiento = mes_día + "-" + str(año_nacimiento)
print(f"Esta es tu fecha de nacimiento '{fecha_nacimiento}'.")
edad = año_actual - año_nacimiento
print(f'Esta es tu edad: {edad}')
vocales = "AEIOUaeiou"
cant_vocales = sum([1 for letra in nombre_completo if letra in vocales])
print(f'Tu nombre completo tiene {cant_vocales} vocales.')
cant_letras = len(nombre_completo)
print(f"Tu nombre completo tiene {cant_letras} letras.")
es_entero = isinstance(edad, int)
print(f'¿Tu edad es un carácter de tipo número? {es_entero}')
es_alfanumerico = nombre_completo.isalnum()
print(f'¿Tu nombre completo es un carácter de tipo alfanumérico? {es_alfanumerico}')
edad_10_anos = edad + 10
print(f'Tu edad en 10 años será {edad_10_anos}.')
print('La media de tu edad actual y tu edad en 20 años es')
