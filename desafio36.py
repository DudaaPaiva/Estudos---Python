'''Programa que lê o salário do comprador, valor da casa quantos anos ele vai pagar. Calcula o valor da prestação sabendo que nao pode ultrapassar 30% do salario'''
salario = float(input('Digite o salário: R$ '))
casa = float(input('Digite o valor da casa: R$'))
anos = int(input('Em quantos vc quer financiar?'))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print(f'Para pagar uma de R$ {casa:.2f} em {anos} anos ', end='')
print(f'a prestação será de {prestacao:.2f}')
if prestacao <= minimo:
  print(f'Empréstimo pode ser concedido')
else:
  print(f'Empréstimo negado')