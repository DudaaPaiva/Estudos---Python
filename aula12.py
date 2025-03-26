nome = str(input('Qual seu nome? '))
if nome == 'Duda':
  print(f'Que nome bonito!')
elif nome == 'Maria' or nome == 'Pedro' or nome == 'Paulo':
  print(f'Seu nome é bem popular no Brasil')
elif nome in 'Ana Claudia Jessica Juliana':
  print (f'Que nome feminino bonito')
else:
  print(f'Seu nome é bem normal.')

print(f'Tenha um bom dia {nome}!')