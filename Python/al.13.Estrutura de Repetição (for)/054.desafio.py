majority = 0
minority = 0

for i in range(0, 7):

    age = int(input('Digite a idade: '))

    if age < 18:
        minority += 1
    else:
        majority += 1

print('Atingiram a maioridade: {}'.format(majority))
print('Não atingiram a maiorideda: {}'.format(minority))