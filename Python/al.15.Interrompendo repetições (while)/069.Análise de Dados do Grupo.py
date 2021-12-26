from colors import color, color_underline_bold

title = color_underline_bold['cyan']
typed_col = color['green']
answer_col = color['blue']
error_col = color['red']
end_col = color['purple']
clean = color['clean']

print(f'\n{title}Cadastro de Pessoas.{clean}\n')

num_old_plaeple = 0
num_new_womam = 0
num_men = 0

i = 0
while True:

    i += 1
    print(f'\n----{i}º PESSOA----')
    age = int(input(f'Digite a idade: {typed_col}'))
    print(end = f'{clean}')

    while True:
        sex = input(f'Digite o sexo[M/F]: {typed_col}').strip().lower()
        print(end = f'{clean}')
        if sex == 'm' or sex == 'f':
            break
        print(f'{error_col}Dados inválidos. Digite "M" ou "F".{clean}\n')

    if age > 18:
        num_old_plaeple += 1

    if sex == 'feminino' or sex == 'f' and age < 20:
        num_new_womam += 1

    if sex == 'masculino' or sex == 'm':
        num_men += 1

    while True:
        p = input(f'\nRealizar outro cadastro?[S/N] {typed_col}').strip().upper()
        print(end = (f'{clean}'))
        if p == 'S' or p == "N":
            break
        print(f'{error_col}Dados inválidos. Digite "S" ou "N".{clean}')

    if p == 'N':
        break

print(f'\n{answer_col}Número de pessoas com mais de 18 anos: {num_old_plaeple}')
print(f'Número de mulheres com menos de 20 anos: {num_new_womam}')
print(f'Número de homens : {num_men}{clean}')
print(f'\n{end_col}Fim do programa.{clean}\n')
