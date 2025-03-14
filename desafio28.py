#Escreva um programa que faça o computador pensar em um numero de 0 a 5 e peça para o usuário advinhar qual foi o numero escolhido. O programa deve mostrar se o usuario acertou ou nao. 
import random
from time import sleep
num = [0,1,2,3,4,5]
computador = random.choice(num) #sorteia um numero 
print(f'-=-'*20)
print(f'Vou pensar em um número entre 0 e 5, tente advinhar...')
print(f'-=-'*20)
usuario = int(input(f'Qual número eu pensei?'))
print(f'Processando...')
sleep(2)
if computador == usuario:
  print(f'Você acertou!')
else:
  print(f'Você errou!Eu pensei em {computador} e vc escolheu {usuario}')

