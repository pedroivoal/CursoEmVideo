from itertools import count
from colors import *

typed_col = color['green']
clean = color['clean']

while True:
    n1 = input(f'Digite um valor inteiro: {typed_col}')
    print(f'{clean}', end = '')
    n = n1.isnumeric()
    if n:
        n1 = int(n1)
        break
while True:
    n2 = input(f'Digite um valor inteiro: {typed_col}')
    print(f'{clean}', end = '')
    n = n2.isnumeric()
    if n:
        n2 = int(n2)
        break
while True:
    n3 = input(f'Digite um valor inteiro: {typed_col}')
    print(f'{clean}', end = '')
    n = n3.isnumeric()
    if n:
        n3 = int(n3)
        break
while True:
    n4 = input(f'Digite um valor inteiro: {typed_col}')
    print(f'{clean}', end = '')
    n = n4.isnumeric()
    if n:
        n4 = int(n4)
        break

tup = (n1, n2, n3 ,n4)

print(f'\nO valor 9 aparece {tup.count(9)} vez(es).')

if 3 in tup:
    p3 = tup.index(3)
    print(f'Posição da 1º aparição do valor 3: {p3}')
else:
    print('Valor 3 não foi digitado.')

print(f'Números pares digitados: ', end = '')
for i in tup:
    if i%2 == 0:
        print(i, end = ' ')
print('\n')

