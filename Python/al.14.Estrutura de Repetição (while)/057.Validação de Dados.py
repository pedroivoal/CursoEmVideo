from colors import color

answer_col = color['blue']
error_col = color['red']
clean = color['clean']

sex = input('\nDigite seu sexo [M/F]: ').strip().upper()

while sex != 'M' and sex != 'F':
    print('\n{}Valor não aceito.{}'.format(error_col, clean))
    sex = input('Digite seu sexo: ').upper()

if sex == 'M':
    print('\n{}Sexo masculino registrado.{}\n'.format(answer_col, clean))
else:
    print('\n{}Sexo feminino registrado.{}\n'.format(answer_col, clean))