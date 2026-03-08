import numpy as np

matriz = np.random.rand(1000, 1000)

# Guardar en formato binario de numpy
np.save("matriz.npy", matriz)

# Cargar después
matriz_cargada = np.load("matriz.npy")
