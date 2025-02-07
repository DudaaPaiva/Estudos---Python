frase = str(input('Digite uma frase: ')).strip().lower()
print('A letra "a" aparece: {} vezes'.format(frase.count('a')))
print(f'A primeira aparição da letra "a" está na posição {frase.find('a')+1}')#esse comando +1 é para mostre no inidice visto por nos, ja q em python começa sempre do zero
print(f'A última aparição da letra "a" está na posição {frase.rfind('a')+1}')

