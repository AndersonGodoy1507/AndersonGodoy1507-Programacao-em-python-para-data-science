import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

dados = pd.read_excel('vendas.xlsx')

df = pd.DataFrame(dados)


media = (df['Vendas']).mean()
print (media)
print('xxxxxxx'*15)

Maior_venda_mes = (df['Vendas']).idxmax()
ma_venda = df.loc[Maior_venda_mes,'Vendas']
mes_maior_venda = df.loc[Maior_venda_mes, 'Meses']
ano_venda = df.loc[Maior_venda_mes,'Ano']
print(mes_maior_venda,ano_venda,ma_venda)

print('xxxxxxx'*15)

menor_venda = (df['Vendas']).idxmin()
m_venda = df.loc[menor_venda,'Vendas']
mes_menos = df.loc[menor_venda,'Meses']
ano_menos = df.loc[menor_venda,'Ano']
print(mes_menos,ano_menos,m_venda)


sns.barplot(data=df, x="Vendas", y="Meses")
plt.show()

print('xxxxxxx'*15)
