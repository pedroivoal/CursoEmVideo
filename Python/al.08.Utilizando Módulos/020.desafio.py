from random import shuffle
n_a = int(input('Digite o número de alunos: '))
while n_a < 1:
    print('O número de alunos deve ser maior que zero.')
    n_a = int(input('Digite o número de alunos: '))

lista_a = [0]*n_a
i = 0

while i < n_a:
    lista_a[i] = input('({})Nome do aluno: '.format(i+1))
    i += 1


shuffle(lista_a)
print('Ordem de apresentação: {} '.format(lista_a))
