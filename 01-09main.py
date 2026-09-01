import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
# import tkinter as tk


def analise():

    dados = pd.read_csv('dados.csv')
    anos = dados['ano']
    vendas = dados['vendas']
    df = pd.DataFrame(dados)

    cores = ['red','green','blue','gold']
    plt.figure(figsize =(6,6))
    plt.pie(df['vendas'],labels =df['ano'],autopct='%1.2f%%', colors= cores)
    plt.show()
    

    # grafico de barras
    plt.figure(figsize= (7,10))
    plt.bar(df['ano'],df['lucro'])
    plt.grid(True)
    plt.show()

    # grafico linha

    plt.figure(figsize=(5,6))
    plt.plot(df['ano'], df['vendas'], marker ='X')
    plt.show()

#grafico correlação (scatter - relaciona 2 variáveis)
    plt.figure(figsize=(5,6))
    plt.plot(df['vendas'], df['lucro'], color = 'orange')
    plt.grid(True)
    plt.show()



analise()
    