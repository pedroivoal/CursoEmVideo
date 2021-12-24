from random import randint

num_al = randint(0, 10)

num_us = int(input('Write a number: '))

if num_al != num_us:
    print('''
    Computador x Você
         {}        {}
    '''.format(num_al, num_us))

tentativas = 1
while num_al != num_us:

    num_al = randint(0, 10)

    num_us = int(input('Write a number: '))
    tentativas += 1

    if num_al != num_us:
        print('''\n
        Computador x Você
            {}        {}
        '''.format(num_al, num_us))

print('Você acertou na {}ª tentativa'.format(tentativas))