import numpy as np
import matplotlib.pyplot as plt

# Configuración de la generación de números aleatorios para reproducibilidad
np.random.seed(3)

# Generar datos aleatorios para el gasto en publicidad (en dólares)
gasto_publicidad = np.random.normal(5000, 1500, 100)

# Generar datos aleatorios para el número de clics en anuncios
clics_anuncios = np.random.normal(1000, 300, 100) - (gasto_publicidad / 1000)

# Crear un diagrama de dispersión (scatter plot) para visualizar los datos
plt.scatter(gasto_publicidad, clics_anuncios)

# Etiquetas de ejes y título
plt.xlabel('Gasto en Publicidad (USD)')
plt.ylabel('Clics en Anuncios')
plt.title('Relación entre Gasto en Publicidad y Clics en Anuncios')

# Mostrar el diagrama de dispersión
plt.show()