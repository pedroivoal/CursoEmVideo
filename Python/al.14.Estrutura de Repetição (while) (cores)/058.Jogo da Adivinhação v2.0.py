from random import randint
from colors import color

# cores para texto 
answer_col = color['blue']
error_col = color['red']
clean = color['clean']

print('\nAdvinhe o número sorteado (0 à 10)')

num_al = randint(0, 10)

num_us = int(input('Digite um número: '))

tentativas = 1
while num_al != num_us:

    if num_us not in range(0, 11):
        print('{}Digite um número inteiro no intervalo [0, 10].{}\n'.format(error_col, clean))
    elif num_us < num_al:
        print('{1}tente um número maior que {0}.{2}\n'.format(num_us, error_col, clean))
    elif num_us > num_al:
        print('{1}tente um número menor que {0}.{2}\n'.format(num_us, error_col, clean))

    num_us = int(input('Digite um número: '))
    tentativas += 1

print('{1}Você acertou na {0}ª tentativa.{2}\n'.format(tentativas, answer_col, clean))