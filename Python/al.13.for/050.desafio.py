s = 0
n = 0

for i in range(0, 6):
    n = float(input('Digite o {}° número: '.format(i+1)))
    if n % 2 == 0:
        s += n

print('A soma dos pares digitados é {}'.format(s))