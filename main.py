print('Sistema de IMC')

altura = float(input('Altura: '))
peso = float(input('Pese: '))

imc= peso / (altura ** 2)


print(imc)

resultado = imc < 18.5 and ('Abaixo do normal') or imc > 18.5 and imc < 25 and ('Peso normal') or ('Acima do Peso')

print(resultado)


