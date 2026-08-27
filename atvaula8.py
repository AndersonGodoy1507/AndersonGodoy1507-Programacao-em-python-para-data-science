#  1. Crie um array de 20 elementos.
import numpy as np

arr = np.arange(21)
# 2. Extraia os primeiros 5 elementos, os últimos 5 
for p in range (5):
    print(p)
print('aaa'*30)
u = arr[-5:]
print(u)
print('aaa'*30)
# elementos e os elementos 
# das posições 5 a 10.
e = arr[5:11]
print(e)
print('aaa'*30)

# Desafio 2:
# 1. Crie duas matrizes 3x3.
# 2. Calcule o produto.
matriz1 =  np.random.randint(0,20,(3,3))
matriz2 = np.random.randint(0,20,(3,3))
print(matriz1)
print('aaa' *30)
print(matriz1)
print('aaa' *30)
produto = np.divide(matriz1,matriz2)
print(produto)
print('aaa' *30)
# Desafio 3:
# Criação de Arrays:

# Crie um array de 1 a 10.
arr1 = np.arange(11)
print(arr1)
# Crie uma matriz 3x3 com valores aleatórios entre 0 e 1.
arr2 =  np.random.randint(0,1,(3,3))
print(arr2)
print('aaa' *30)

# Desafio 4:
# Calcule a soma dos elementos do array.
# Encontre o valor máximo e mínimo do array.
soma = np.sum(arr2)
print(soma)
print('aaa'*30)

# Desafio 5:
# Calcule a média dos valores do array.
# Calcule a mediana dos valores do array.
media = np.mean(arr2)
mediana = np.median(arr2)
print(media)
print(mediana)