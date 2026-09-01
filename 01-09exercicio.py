# 2 - Crie um gráfico plot para mostra:
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np

# 2 - Crie um gráfico plot para mostra:

ano = [2021,2022,2023,2024,2025,2026]

vendas = [10000,2000,30000,10000,5000,20000]


plt.figure(figsize=(5,6))
plt.plot(ano,vendas, marker ='X')
plt.grid(True)
plt.show()

# ***3 - Desenvolva em gráfico  barras:***

medias_jose = [10,5,8,9,10,5,4]
meses = ['feve','març','abril','maio','jun','jul','agos']
plt.figure(figsize= (7,10))
plt.bar(meses,medias_jose)


plt.show()

medias_jose = [10,5,8,9,10,5,4]
meses = ['feve','març','abril','maio','jun','jul','agos']

plt.figure(figsize = (6,6))
plt.pie(medias_jose,labels = meses,autopct='%1.1f%%')
plt.show()