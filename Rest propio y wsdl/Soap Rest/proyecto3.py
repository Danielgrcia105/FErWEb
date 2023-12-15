from bs4 import BeautifulSoup
import requests
import pandas as pd
 
years = [1930, 1934, 1938, 1950, 1958, 1962, 1966, 1970, 1974, 1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018]
 
web = 'https://es.wikipedia.org/wiki/Copa_Mundial_de_F%C3%BAtbol_de_2022'
Respuesta = requests.get(web)
coontenido = Respuesta.text
soup = BeautifulSoup(coontenido, 'lxml')
matches = soup.find_all('div', class_='collapsible autocollapse vevent plainlist')
 
home = []
score = []
Visit = []
 
for match in matches:
    home.append(match.find('span', class_='flagicon').get_text())
    score.append(match.find('div', class_='87.13 x 22.39').get_text())
    Visit.append(match.find('span', class_='flagicon').find_next('a').get_text())
 
dict_Foall = {'home': home, 'score': score, 'Visit': Visit}
df_fooatball = pd.DataFrame(dict_Foall)
 
df_fooatball['years'] = years
 
df_fooatball['fifa'] = df_fooatball['years'].apply(lambda x: "FIFA" if x in years else "")
 
df_fooatball.to_csv('fifa-world-cup-historial_data.csv', index=False)
 
print(df_fooatball)