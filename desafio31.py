#Programa que calcula o preço de uma viagem de ate 200 km me 0,50 por km e acima disso fica 0,45
distancia = float(input('Qual a distancia da sua viagem? '))
if distancia <= 200:
  valor = distancia * 0.50
  print(f'Sua viagem foi menos de 200 km, então o valor da sua viagem custa R$ {valor:.2f}')
else:
  valor = distancia * 0.45
  print(f'Sua viagem foi longa e você teve um desconto, o valor fica R$ {valor:.2f}')