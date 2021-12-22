from time import sleep

print('Carregando...')

i = 0
while i < 10:
    print('{}...'.format(i+1))
    i += 1
    sleep(0.25)
print()

c = -1
Sum = 0
while i != 0:
    i = int(input('Idade: '))
    Sum += i
    c += 1

med = Sum/c
print('\nMédia: {}'.format(med))
print('O último valor não é considerado\n')