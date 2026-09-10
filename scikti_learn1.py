# from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# venda = {
#     'jan':20000.0,
#     'fev':30000.0,
#     'mar':50000.0,
# }


# meses = np.array([1,2,3]).reshape(-1,1)
# valores = np.array([20000.0,30000.0,50000.0])

# modelo = LinearRegression()
# modelo.fit(meses,valores)

# proximo_mes = 4
# venda_prevista = modelo.predict([[proximo_mes]])[0]
# print('Previsao: ', venda_prevista)


# horas_estudos = np.array([2,4,6,8,10]).reshape(-1,1)

# notas = np.array([4,4.4,5,7.5,8])


# modelo = LinearRegression()
# modelo.fit(horas_estudos,notas)

# hora_estudo = 7

# previsao = modelo.predict([[hora_estudo]])[0]
# print(previsao)



# from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
import numpy as np


frutas_caracteristicas  =  np.array([[7,150],[8,170], [6,130], [9,180], [5,120]])
classes_frutas  =  np.array([0,0,1,0,1])


modelo = KNeighborsClassifier(n_neighbors=3)
modelo.fit(frutas_caracteristicas, classes_frutas)



nova_ = np.array([[9,720]])
classifica = modelo.predict(nova_)[0]


tipo = 'maça' if classifica == 0 else 'laranja'


print(tipo)





