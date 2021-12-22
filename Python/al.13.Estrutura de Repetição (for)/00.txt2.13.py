ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))

for i in range(ini, fim, pas):
    print('{:.0f}'.format(i), end = ', ' )
    if i%20 == 0:
        print()

print('{}.'.format(i+1))