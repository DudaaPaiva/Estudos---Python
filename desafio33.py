#programa que le 3 números e determina qual deles é o menor 
primeiro = int(input('Digite o primeiro número:'))
segundo = int(input('Digite o segundo número:'))
terceiro = int(input('Digite o terceiro número:'))
numeros = [primeiro, segundo, terceiro]

print(f'O maior valor digitado foi {max(numeros)}')
print(f'O menor numero digitado foi {min(numeros)}')