nome = str(input('Digite o nome completo: ')).strip().split()
print(f'Seu primeiro nome é: {nome[0]}')
print(f'Seu último nome é: {nome[len(nome)-1]}')