
name=input ('¿Cuál es tu nombre?')
papellido=input('¿Cuál es tu primer apellido?')
sapellido=input('¿Cuál es tu segundo apellido?')
año_nacimiento=input('¿En qué año naciste?')
mes_día=input('¿En qué mes y día naciste? (en el siguiente formato “mm-dd”)')
año_actual=2022
edad = año_actual - año_nacimiento

nombre_completo = name + "" + papellido + sapellido
print('Este es tu nombre completo en mayúsculas:' + nombre_completo)
print('Este es tu nombre completo en minúsculas:' + nombre_completo)
print('Esta es tu fecha de nacimiento “dd-mm-aaaa”:' +  mes_día + '-' + año_nacimiento)
print('Esta es tu edad:'+  edad)
print('Tu nombre completo tiene' + + 'vocales.')
print('Tu nombre completo tiene' + + 'letras')
print('¿Tu edad es un carácter de tipo número?'+ '__True__')
print('¿Tu nombre completo es un carácter de tipo alfanumérico?'+ '__True__')
print('Tu edad en 10 años será'+ edad + 10)
print('La media de tu edad actual y tu edad en 20 años es')
