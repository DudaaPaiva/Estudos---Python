dias = int(input('Digite a quantidade de dias alugados: '))
km = float(input('Digite a quantidade de kms rodados: '))
aluguel = (dia * 60) + (km * 0.15)
print('O valor a ser pago de aluguel é R${:.2f}'.format(aluguel))