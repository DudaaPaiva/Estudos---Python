num = int(input('Digite o numero entre 0 e 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'A unidade é: {u}')
print(f'A dezena é: {d}')
print(f'A centena é: {c}')
print(f'O milhar é: {m}')

