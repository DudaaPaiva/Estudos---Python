from random import choice
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segudno aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4] #Lista em python está sempre entre colchetes
escolhido = choice(lista)
print('O aluno escolhido foi: {}'.format(escolhido))