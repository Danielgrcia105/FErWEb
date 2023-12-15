import numpy as np
import matplotlib.pyplot as plt

# Datos de ejemplo
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 2.5, 4, 3.5])

# Resto del código (mezcla aleatoria y división en conjuntos de entrenamiento/prueba)
indices_mezclados = np.random.permutation(len(x))
x_mezclado = x[indices_mezclados]
y_mezclado = y[indices_mezclados]

tamanio_entrenamiento = int(0.8 * len(x_mezclado))
tamanio_prueba = len(x_mezclado) - tamanio_entrenamiento

tren_x = x_mezclado[:tamanio_entrenamiento]
tren_y = y_mezclado[:tamanio_entrenamiento]

prueba_x = x_mezclado[tamanio_entrenamiento:]
prueba_y = y_mezclado[tamanio_entrenamiento:]

# Mostrar el diagrama de dispersión con el conjunto de entrenamiento
plt.scatter(tren_x, tren_y)
plt.show()

# Mostrar el diagrama de dispersión con el conjunto de prueba
plt.scatter(prueba_x, prueba_y)
plt.show()