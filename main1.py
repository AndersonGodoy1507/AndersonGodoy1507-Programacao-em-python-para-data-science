#E-commerce


print('e-commerce')

login = input('Digite seu Login :')
senha = input('Digite sua senha :')

carrinho =  []
total = []
produtos = ['computador','mesa','hd','tenis']
valores = [5000,252.25,500.55,540.66]

prod1= int(input('Escolha o ID do produto: 0,1,2,3'))
prod2= int(input('Escolha o ID do produto: 0,1,2,3'))
prod3= int(input('Escolha o ID do produto: 0,1,2,3'))

carrinho.append(produtos[prod1])
carrinho.append(produtos[prod2])
carrinho.append(produtos[prod3])

total.append(produtos[prod1])
total.append(produtos[prod2])
total.append(produtos[prod3])

soma = sum(total)
print('R$')
print('Produtos :')
print(total)



# e-commerce


print('e-commerce ')


login = input('Digite seu Login: ')
senha  =  input('Digite senha: ')


carrinho = []
total = []
produtos  =  ['computador', 'mesa', 'hd', 'tenis']
valores = [5000,250.25,500.55,540.66]


prod1 =  int(input('Escolha o ID do produto:  0,1,2,3'))
prod2 =  int(input('Escolha o ID do produto:  0,1,2,3'))
prod3 =  int(input('Escolha o ID do produto:  0,1,2,3'))


carrinho.append(produtos[prod1])
carrinho.append(produtos[prod2])
carrinho.append(produtos[prod3])


total.append(valores[prod1])
total.append(valores[prod2])
total.append(valores[prod3])


soma =  sum(total)
print('R$')
print(soma)
print('Produtos:')
print(carrinho)