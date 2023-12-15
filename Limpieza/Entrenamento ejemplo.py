import numpy as np
from sklearn.linear_model import LinearRegression

# Datos de entrenamiento
# Área de las casas en metros cuadrados
X_train = np.array([60, 80, 100, 120, 150, 180, 200, 220, 300]).reshape(-1, 1)

# Precio de las casas en miles de dólares
y_train = np.array([100, 150, 200, 230, 280, 320, 350, 400, 450])

# Crear modelo de regresión lineal
model = LinearRegression()

# Entrenar el modelo con los datos de entrenamiento
model.fit(X_train, y_train)

# Hacer predicciones en nuevos datos
# Supongamos que queremos predecir el precio de una casa de 180 metros cuadrados
X_new = np.array([180]).reshape(-1, 1)
y_pred = model.predict(X_new)

print("Precio predicho para una casa de 180 metros cuadrados en dolares:", y_pred[0])