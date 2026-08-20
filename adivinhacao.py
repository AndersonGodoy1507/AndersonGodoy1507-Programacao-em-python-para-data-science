import random

def display():
    print('Adivinhe o numero!!! ')

def roda_numero(lista):
    
     numero = random.choice(lista)
     return numero
display()    

def ecolha_numero():
  lista  = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
  escolha = -1
  roda = roda_numero(lista)
  
  while escolha != 0: 
         escolha = int(input('Escolha seu número de 1 até 15 , não vale 0'))
    
         if escolha == roda:
            print('Acertou o numero é; ',escolha)
         elif escolha > roda:
            print('O número é menor')
         else:
            print('O número é menor')
         
 
  
ecolha_numero() 
       
    
        

     
     