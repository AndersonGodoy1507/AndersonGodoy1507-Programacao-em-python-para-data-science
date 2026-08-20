def display():
    print('Sistemas de médias alunos')

def media(n1,n2,n3,n4):
    return (n1 + n2 + n3 + n4) / 4

def sis_calc_media():
    display()
    nome =input('Digite o nome do Aluno: ')
    n1 = float(input('Digite a nota primeiro bimestre: '))
    n2 = float(input('Digite a nota segundo bimestre: '))
    n3 = float(input('Digite a nota terceito bimestre: '))
    n4 = float(input('Digite a nota quartobimestre: '))
    nota_final = media(n1,n2,n3,n4)
    if nota_final >= 6:
        print('A média do aluno(a):', nome, 'é:', nota_final,'e está aprovado!')
    else:
         print('A média do aluno(a): ,', nome, 'é:', nota_final,'e estáreprovado!')


sis_calc_media()
