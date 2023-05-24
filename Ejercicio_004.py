import numpy as np

# Definir las matrices A y B.
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[-1, 0], [0, 1], [1, 1]])

# Calculamos el producto de las matrices.
producto = np.dot(A, B)

# Imprimimos el producto de las matrices.
print("El producto de las matrices es:\n", producto)
