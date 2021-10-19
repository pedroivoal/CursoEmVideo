print('''Digite
2 para ver o número digitado na base binária.
8 para ver o número digitado na base octonal.
16 para ver o número digitado na base hexadecimal.''')
v = int(input('Digite a base: '))
num = int(input('\nDigite um número: '))

if v == 2:
    print(num)
#elif v == 8:

#elif v == 16:

else:
    print('\nEssa base não é comvertida pelo programa.')