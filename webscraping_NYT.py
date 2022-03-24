import requests
import pandas as pd

texto_string = requests.get('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html').text
print(texto_string[:100])


from bs4 import BeautifulSoup

bsp_texto = BeautifulSoup(texto_string, 'html.parser')
lista_noticias = bsp_texto.find_all('span', attrs={'class':'short-desc'})
print(type(bsp_texto))
print(type(lista_noticias))
print(lista_noticias[5])

dados=[]
for noticia in lista_noticias:
    data = noticia.contents[0].text.strip() + ', 2017'
    comentario = noticia.contents[1].strip().replace("“",'').replace("”", '')
    explicacao = noticia.contents[2].text.strip().replace("(", '').replace(")", '')
    url = noticia.find('a')['href']
    dados.append((data, comentario, explicacao, url))

print(dados[1])

df_noticias = pd.DataFrame(dados, columns=['data','comentario','explicacao','url'])
print(df_noticias.shape)
print(df_noticias.dtypes)
print(df_noticias.head())