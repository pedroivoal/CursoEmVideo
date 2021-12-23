from colors import col

n1 = float(input('Digite um número: '))
n2 = float(input('Digite um número: '))
c = 0

while True:
    print('''
[1]-Somar
[2]-Multiplicar
[3]-Maior
[4]-Novos Números
[5]-Sair do Programa''')

    c = int(input())

    if c == 1:
        r = n1 + n2
        print('{3}{0} + {1} = {2}{4}'.format(n1, n2, r,col['blue'], col['clean']))
    elif c == 2:
        r = n1*n2
        print('{3}{0} . {1} = {2}{4}'.format(n1, n2, r,col['blue'], col['clean']))
    elif c == 3:
        r = max(n1,n2)
        print('{1}Maior número: {0}{2}'.format(r,col['blue'], col['clean']))
    elif c == 4:
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite um número: '))
    elif c == 5:
        print('{0}Fim do programa{1}\n'.format(col['green'], col['clean']))
        break
    else:
        print('\n{0}Escolha um número entre 1 e 5.{1}\n'.format(col['red'], col['clean']))

         