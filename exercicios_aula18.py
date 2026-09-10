import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import tkinter as tk



# EXERCICIO 1: Previsão de Notas Escolares

import numpy as np
from sklearn.linear_model import LinearRegression

# Dados históricos de horas de estudo vs notas
horas_estudo = np.array([2, 4, 6, 8, 10]).reshape(-1, 1)
notas = np.array([5.0, 6.5, 7.8, 8.5, 9.2])

modelo = LinearRegression()
modelo.fit(horas_estudo,notas)


hora_estudo = 11

previsao = modelo.predict([[hora_estudo]])[0]

print(previsao)
print('Exercicio 1')

# EXERCICIO 2: Previsão de Consumo de Energia

# dados de temperatura x consumo de energia
temperaturas = np.array([15, 20, 25, 30, 35]).reshape(-1, 1)
consumo_kwh = np.array([120, 100, 90, 110, 150])


modelo1 = LinearRegression()
modelo1.fit(temperaturas,consumo_kwh)

temp = 40

previsao1 = modelo1.predict([[temp]])[0]
print(previsao1)
print('Exercicio 2')


#EXERCICIO 3: Previsão de Crescimento de Plantas

# Dados de dias desde plantio vs altura da planta
dias = np.array([10, 20, 30, 40, 50]).reshape(-1, 1)
altura_cm = np.array([5, 12, 18, 25, 30])

modelo2 = LinearRegression()
modelo2.fit(dias,altura_cm)


dias = 40

previsao2 = modelo2.predict([[dias]])[0]
print(previsao2)
print('Exercicio 3')

# EXERCICIO 4:Dados de quantidade de fertilizante vs produção
fertilizante_kg = np.array([50, 100, 150, 200, 250])
producao_ton = np.array([2.0, 3.5, 4.8, 5.5, 6.0]).reshape(-1, 1)

modelo3 = LinearRegression()
modelo3.fit(producao_ton,fertilizante_kg)

ton = 20

previsao3 = modelo3.predict([[ton]])[0]
print(previsao3)