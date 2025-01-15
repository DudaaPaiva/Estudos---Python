n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2 
di = n1 // n2
e = n1 ** n2 
print('A soma é {}, a multiplicação é {} e a divisão é {:.3f}'.format(s, m ,d), end=' ') #{:.3f} é para formatar a saida com 3 casas flutuantes
#comando ,end='' serve para juntar dois prints numa mesma linha, \n serve para quebrar a linha no meio da frase.
print('Divisão inteira é {} e potência {}'.format(di, e))