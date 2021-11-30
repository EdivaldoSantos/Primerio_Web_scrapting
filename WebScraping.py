# Documentação sobre o BeautifulSoup https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/#
# Importação das bibliotecas
import requests
import pandas as pd
from bs4 import BeautifulSoup
import re


# Criando lista de links e categorias
links = []
categoria = []

# Busca dos links e categorias
paginas = requests.get('http://books.toscrape.com')
if paginas.status_code == 200:
    print('Requisição bem sucedida!')
    content = paginas.content

page_html = BeautifulSoup(content, 'html.parser')
url = page_html.find_all(attrs={'class': 'side_categories'})


for url in url:
    links.append(url.find_all('a',))

    print(links)
# Teste
