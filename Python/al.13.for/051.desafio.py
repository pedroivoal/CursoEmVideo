a1 = float(input('Digite a1: '))
r = float(input('Digite a razão: '))

for i in range(0, 10):
    print('{}° termo = {:.0f}'.format(i+1, a1))
    a1 += r