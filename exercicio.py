

# 1- APÓS APLIQUE COM O MÓDULO STATISTICS DO PYTHON, CRIANDO SEUS PRÓPRIOS MÓDULOS COM O AUXILIO DA BIBLIOTECA STATISTICS:

# Precisa ter 2 arquivos o #main e o #funcoes.

# Utilize funções** -  Crie seu próprio módulo.

# Crie 3  função utilizando a importação da statistics 

# precisa ter a criação da sua função e a utilização do módulo statistics.

# 1 - FREQUENCIA  =  [1,2,3,6,4]

# 2 - FREQUENCIA  =  [1.5,6.8,9.7,10.6]

# 3 - FREQUENCIA  =  [200,300,500,700,900,400,600]

# 1 - MEÇA A MODA 

# 2 - MEDIANA

# 3 - MÉDIA
1

import statistics


def estatistica():


  while True:
    n = int(
        input(
            'Escolha uma ação: 1 - Média, 2 - Mediana, 3 - Moda, 0 - Sair: '
        )
    )

    if n == 0:
      print('Saindo...')
      break
    elif n == 1:
      f1 = [200, 300, 500, 700, 900, 400, 600]
      media = statistics.mean(f1)
      print(media)
    elif n == 2:
      f2 = [1.5, 6.8, 9.7, 10.6]
      mediana = statistics.median(f2)
      print(mediana)
    elif n == 3:
      f3 = [1, 2, 3, 6, 4]
      moda = statistics.mode(f3)
      print(moda)
    else:
      print('Opção inválida. Tente novamente.')

estatistica()



