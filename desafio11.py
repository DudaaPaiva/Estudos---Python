altura = float(input('Altura da parede: '))
largura = float(input('Largura da parede:'))
area = altura * largura 
tinta = area / 2 #1 litro de tinta pinta 2m² 

print('Sua parede tem a dimensão de {} x {} e sua área é de {:.2f}m²'.format(altura, largura, area))
print('Para pintar sua parede você precisará de {:.2f}l de tinta'.format(tinta))
