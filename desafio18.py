from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo: '))
seno = sin(radians(angulo))#radians serve para converter em radianos, sem essa conversao o calculo n funciona
print('O ângulo de {} tem o seno de {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O ângulo de {} tem a tangende de {:.2f}'.format(angulo, tangente))