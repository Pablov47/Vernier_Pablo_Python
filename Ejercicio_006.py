#ejercicio6
import math

def area_circulo(radio):
    """Esta función calcula el área de un círculo dado su radio."""
    return math.pi * radio ** 2

def volumen_cilindro(radio, altura):
    """Esta función calcula el volumen de un cilindro dado su radio y altura."""
    return area_circulo(radio) * altura

print("El área del círculo es", area_circulo(5))
print("El volumen del cilindro es", volumen_cilindro(5, 10))