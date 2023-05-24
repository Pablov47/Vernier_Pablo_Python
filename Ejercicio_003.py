#Ejercicio 3
# Almacenar la contraseña en una variable, que en este caso será "qwerty123"
contrasena_correcta = "qwerty123"

# Iniciar una variable para la contraseña de un usuario.
contrasena_usuario = ""

# Mientras la contraseña del usuario no sea correcta, seguimos pidiendo una contraseña.
while contrasena_usuario != contrasena_correcta:
    contrasena_usuario = input("Introduce la contraseña correcta: ")

print("¡Contraseña correcta ingresada!")
