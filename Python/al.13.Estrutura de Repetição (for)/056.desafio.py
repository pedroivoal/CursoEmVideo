num_new_womam = 0
Sum = 0
age_older_man = 0
name_older_man = ''

for i in range(0, 4):

    print('\n----{}º PESSOA----'.format(i+1))
    name = input('Digite o nome: ').title()
    age = int(input('Digite a idade: '))
    sex = input('Digite o sexo: ').lower()

    Sum += age

    if sex == 'feminino' or sex == 'f' and age < 20:
        num_new_womam += 1

    if sex == 'masculino' or sex == 'm' and age > age_older_man:
        age_older_man = age
        name_older_man = name

print('\nMédia das idades: {}'.format(Sum/4))
print('Homem mais velho: {}'.format(name_older_man))
print('Número de mulheres com menos de 20 anos: {}'.format(num_new_womam))