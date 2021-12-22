from random import randint

print('Advinhe o número sorteado (0 à 10)')

num_al = randint(0, 10)

num_us = int(input('Digite um número: '))

tentativas = 1
while num_al != num_us:

    print('Número incorreto, tente novamente.\n')

    num_us = int(input('Digite um número: '))
    tentativas += 1

print('Você acertou na {}ª tentativa.'.format(tentativas))