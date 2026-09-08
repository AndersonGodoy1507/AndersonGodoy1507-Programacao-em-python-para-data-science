

# # URL da página que você deseja extrair os dados
# url = 'http://quotes.toscrape.com/'

# # Realiza a requisição HTTP para obter o conteúdo da página
# response = requests.get(url)

# # Cria um objeto BeautifulSoup e especifica o parser
# soup = BeautifulSoup(response.text, 'lxml')

# # Encontra todas as citações na página
# quotes = soup.find_all('div', class_='quote')

# # Itera sobre as citações e extrai o texto, autor e tags
# for quote in quotes:
#     text = quote.find('span', class_='text').get_text()
#     author = quote.find('small', class_='author').get_text()
#     tags = [tag.get_text() for tag in quote.find_all('a', class_='tag')]
   
#     print(f'Texto: {text}')
#     print(f'Autor: {author}')
#     print(f'Tags: {tags}')
#     print('-' * 40)

import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 


url = "https://gratuitos.netlify.app/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

tabela = soup.find_all('div', class_ = 'table-responsive')

for linha in tabela:
    print(linha.text)
