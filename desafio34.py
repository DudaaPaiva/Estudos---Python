# programa que le um salario e calcula o aumento de acordo com o valor desejado
salario = float(input('Digite o salário R$ '))
if salario <= 1250:
    novoSalario = salario + (salario * 15 / 100)
    print(f'O salário com 15% de aumento é R$ {novoSalario:.2f}')
else:
    novoSalario = salario + (salario * 10/100)
    print(f'O salário com 10% de aumento é R${novoSalario:.2f}')
