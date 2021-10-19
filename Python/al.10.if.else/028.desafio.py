from random import randint
from time import sleep

num_al = randint(0, 5)

num_us = int(input('Write a number: '))
print('Processando...')
sleep(2)
if num_al == num_us:
    print('You are right.')
else:
    print('You are wrong.')
print('{} != {}'.format(num_al, num_us))