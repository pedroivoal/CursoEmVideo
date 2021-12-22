sex = input('Digite seu sexo [M/F]: ').upper()

while sex != 'M' and sex != 'F':
    print('\nValor não aceito')
    sex = input('Digite seu sexo: ').upper()

if sex == 'M':
    print('\nHomens a esquerda.')
else:
    print('\nMulheres a direita.')