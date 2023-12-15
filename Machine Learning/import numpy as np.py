import numpy as np
import pandas as pd 
import matplotlib.pyplot as pit
from sklearn.linear_model import LinearRegression

datos = pd.read_excel("C:/Users/Alumno.D-LAB2-20-05742/Documents/Python/reduccion.xlsx")
print (datos)

x = datos [("Reduccion de solidos")]
#print (x)

y = datos [("Reduccion de la demanda de oxigeno")]
#print (y)

pit.scatter(x,y)
pit.xlabel("Reduccion de solidos")
pit.ylabel("Reduccion de la demanda de oxigeno")
pit.grid()
pit.show()
matriz = datos.to_numpy ()
print(datos)
