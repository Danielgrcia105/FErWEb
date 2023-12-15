import pandas as pd
from string import ascii_uppercase as abecedario
import pickle
Datos_tablas = pd.read_html('https://es.wikipedia.org/wiki/Copa_Mundial_de_F%C3%BAtbol_de_2022')
print (Datos_tablas[8])
print(Datos_tablas[15])
print(Datos_tablas[22])
 
for letra, i in zip(abecedario, range (8,15,22)):
    print(letra, i )
   
Datos_tablas= pd.read_html('https://es.wikipedia.org/wiki/Copa_Mundial_de_F%C3%BAtbol_de_2022')
dict_tablas = {}
for letra, i in zip (abecedario, range (8,15,7)):
    Datos= Datos_tablas [i]
    Datos.rename(colums = {Datos.columns[1]: "Equipo"}, inplace = True)
    Datos.pop('Selección')
print (i)
dict_tablas ['Grupo H']
with open('dit_teable', 'wb')as output:
  pickle.dumb(dict_tablas, output)