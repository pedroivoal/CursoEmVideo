from random import randint
n_a = int(input('Digite o número de alunos: '))
while n_a < 1:
    print('O número de alunos deve ser maior que zero.')
    n_a = int(input('Digite o número de alunos: '))

lista_a = [0]*n_a
i = 0

while i < n_a:
    lista_a[i] = input('({})Nome do aluno: '.format(i+1))
    i += 1


sort = randint(0, n_a-1)

print('{} apague o quadro.'.format(lista_a[sort]))


'''from random import randint
lista_a = [0]*4

lista_a[0] = input('(1)Nome do aluno: ')
lista_a[1] = input('(2)Nome do aluno: ')
lista_a[2] = input('(3)Nome do aluno: ')
lista_a[3] = input('(4)Nome do aluno: ')

i = randint(0, 3)

print('{} apague o quadro.'.format(lista_a[i]))'''