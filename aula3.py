n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2 
#print('A soma entre', n1, ' e ',n2, 'vale ', s) dessa forma funciona, porém a outra sintaxe é a mais atual
print('A soma entre {} e {} vale {}'.format(n1, n2, s))