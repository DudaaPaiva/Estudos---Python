from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa mede {:.2f}'.format(hi))





# Resolvido usando formula matemática 
'''co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('O cateto oposto é {}, o cateto adjacente é {} e hipotenusa é {:.2f}'.format(co, ca, hi))'''