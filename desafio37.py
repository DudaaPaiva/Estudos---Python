#Programa que lê um número inteiro e converte em binario, octal ou hexadecimal 
num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] para converter para BINÁRIO
[2] para converter para OCTAL
[3] para converter para HEXADECIMAL ''')
opcao = int(input('Sua opção: '))
if opcao == 1:
  print(f'O número {num} convertido para BINÁRIO é igual a {bin(num)[2:]}')
elif opcao == 2:
  print(f'O número {num} convertido para OCTAL é igual a {oct(num)[2:]}')
elif opcao == 3:
  print(f'O número {num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')
else:
  print(f'Opção inválida. Digite um número entre 1 e 3')