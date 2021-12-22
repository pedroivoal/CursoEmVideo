n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if max(n1, n2) == n1 and n1 != n2:
    print('\nO primeiro valor, {}, é maior.'.format(n1))
elif max(n2, n2) == n2 and n1 != n2:
    print('\nO segundo valor, {}, é maior.'.format(n2))
else:
    print('\nOs dois são iguais.')
