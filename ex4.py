n = (input('Digite algo: '))
print('O tipo primitivo desse valor é ', type(n))
print('Só tem espaços?', n.isspace())
print('É um número?', n.isnumeric())
print('Está em maiuscúla?', n.isupper())
print('É alfabético?', n.isalpha())
print('É alfanúmerico?', n.isalnum())
print('Está em minuscúla?', n.islower())
print('Está capitalizada?', n.istitle())#Palavra que tem a primeira letra maiuscúla