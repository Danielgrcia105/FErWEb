import numpy as np
from sklearn.metrics import r2_score
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Datos de ejemplo
minutos_en_tienda = np.array([10, 20, 30, 40, 50])
dinero_gastado = np.array([50, 100, 150, 200, 250])

# Crear un objeto PolynomialFeatures para generar características polinómicas de grado 2
poly_features = PolynomialFeatures(degree=2)
minutos_en_tienda_poly = poly_features.fit_transform(minutos_en_tienda.reshape(-1, 1))

# Crear y entrenar el modelo de regresión lineal con características polinómicas
modelo = LinearRegression()
modelo.fit(minutos_en_tienda_poly, dinero_gastado)

# Hacer predicciones en los mismos datos de entrada para el gráfico
predicciones = modelo.predict(minutos_en_tienda_poly)

# Calcular R^2
r_cuadrado = r2_score(dinero_gastado, predicciones)

print("Coeficiente de determinación (R^2):", r_cuadrado)