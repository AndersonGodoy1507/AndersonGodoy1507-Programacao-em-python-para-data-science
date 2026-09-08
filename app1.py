import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 


# url = "https://gratuitos.netlify.app/"
# headers = {"User-Agent": "Mozilla/5.0"}
# response = requests.get(url, headers=headers)
# soup = BeautifulSoup(response.text, "html.parser")


# tabela = soup.select_one("div.table-responsive table")

# for linha in tabela.find_all("tr"):
#     dados = [c.text.strip() for c in linha.find_all(["th", "td"])]
#     if dados:
#         print(dados)




url = "https://gratuitos.netlify.app/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

tabela = soup.find_all('div', class_ = 'card')

for linha in tabela:
    print(linha.text) 
