#Escreva um programa que leia a velocidade de um carro, se ultrapassar 80km/h mostre uma mensagem dizendo q foi multado em 7$ por km excedente. 
velocidade = float(input(f'Qual velocidade o carro está? '))
if velocidade > 80:
  print(f'Você foi multado por estar acima de 80km/h!')
  multa = (velocidade-80)*7
  print(f'Você deve pagar R${multa:.2f} ')
else:
  print(f'Tenha um bom dia!')
