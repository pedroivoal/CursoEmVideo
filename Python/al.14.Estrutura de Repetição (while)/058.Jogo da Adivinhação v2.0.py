from random import randint
from colors import color

answer_col = color['blue']
error_col = color['red']
clean = color['clean']

print('\nAdvinhe o número sorteado (0 à 10)')

num_al = randint(0, 10)

num_us = int(input('Digite um número: '))

tentativas = 1
while num_al != num_us:

    print('{}Número incorreto, tente novamente.{}\n'.format(error_col, clean))

    num_us = int(input('Digite um número: '))
    tentativas += 1

print('{1}Você acertou na {0}ª tentativa.{2}\n'.format(tentativas, answer_col, clean))