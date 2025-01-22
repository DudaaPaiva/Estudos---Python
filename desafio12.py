preco = float(input('Qual o preço do produto? R$ '))
novo = preco - (preco * 5 / 100) # para calcular o valor do desconto 
print('O produto custava R${:.2f}, na promoção com 5% vai custar R${:.2f}'.format(preco, novo))