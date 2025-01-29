#Manipulação de texto 

'''Ao criar uma variavel do tipo string em python cada palavra equivale a uma posição num indice iniciado a partir da posição 0.'''

#Fatiamento: 
frase = 'Curso em Video Python'
print(frase[20]) #nesse comando pega apenas o caracter q esta na posição 20, no caso n
print(frase[:20:2]) #aqui vai ate o caracter 20 pulando de dois em dois
print(frase[:5])# aq o intervalo entre o inicio e o caracter 5
print(frase[5:])# intervalo entre 5 e o fim da frase
print(frase[9::3])# intervalo a partir do numero nome, indo ate o final pulando de 3 em 3

#Analise
tamanho = len(frase) # esse comando conta a quantidade de caracteres dentro de uma string
print(f'O comprimento da frase é: {tamanho}')
print(frase.count('o'))# esse comando conta e exibe na tela a quantidade de certa letra em uma frase
print(frase.count('o',0,14))# fazendo dessa forma ja fatia e faz a contagem no intervalo desejado
print(frase.find('deo'))# mostra em qual indice começou determinada palavra
print('Curso' in frase)# operador in para verificar se existe a palavra na string 

#Transformação
texto = '   Aprenda Python  '
print(frase.replace('Python', 'Android')) #localiza a palavra fornecida no primeiro argumento e substitui pelo segundo
print(texto.upper())#deixa todas as letras da string em maiusculas
print(texto.lower())#deixa todas as letras da string em minusculas
print(texto.lower().find('python'))#indica em qual posição do indice a palavra desejada está
print(texto.capitalize())#deixa apenas a primeira letra maiuscula e as outras minusculas
print(texto.title())#deixa a primeira letra de cada palavra maiúscula 
print(texto.strip())#remove espaços inuteis tanto do começo quanto do final da string
print(texto.rstrip())#remove espaços inuteis da direita da string
print(texto.lstrip())#remove espaços inuteis da esquerda da string

#Divisão de string 

print(frase.split())#comando que divide a string em lista cada um com um indice
dividido = frase.split()#cria uma variavel que recebe a lista
print(dividido[0])#printa so a primeira palavra da string
print('-'.join(frase.split()))#comando separa e poe traços em cada palavra 