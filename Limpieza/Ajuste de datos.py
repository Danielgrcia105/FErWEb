import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

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

# Crear un objeto PolynomialFeatures para generar características polinómicas
grado_del_polinomio = 2  # Puedes ajustar el grado del polinomio según tu elección
poly_features = PolynomialFeatures(degree=grado_del_polinomio)

# Transformar las características originales en características polinómicas
tren_x_poly = poly_features.fit_transform(tren_x.reshape(-1, 1))

# Crear y entrenar el modelo de regresión lineal con características polinómicas
modelo = LinearRegression()
modelo.fit(tren_x_poly, tren_y)

# Generar valores para la curva de regresión polinómica
x_valores = np.linspace(min(x), max(x), 100)  # Valores de x para la curva
x_valores_poly = poly_features.transform(x_valores.reshape(-1, 1))  # Transformar para el modelo
y_pred = modelo.predict(x_valores_poly)  # Predicciones

# Visualizar los datos de entrenamiento y la curva de regresión polinómica
plt.scatter(tren_x, tren_y, label='Datos de entrenamiento')
plt.plot(x_valores, y_pred, color='red', linewidth=2, label='Regresión Polinómica')
plt.xlabel('Variable Independiente')
plt.ylabel('Variable Dependiente')
plt.legend()
plt.show()