from colors import color ,color_underline_bold

title = color_underline_bold['cyan']
typed_col = color['green']
answer_col = color['blue']
error_col = color['red']
end_col = color['purple']
clean = color['clean']

print(f'\n{title}Gerador de Tabuadas{clean}\n')
print('Para finalizar o programa digite um número negativo.')

while True:

    n = int(input(f'\nDigite um valor: {typed_col}'))
    print(end = f'{clean}')

    if n < 0:
        break

    i = 1
    while i < 11:

        print(f'{answer_col}{n} x {i} = {n*i}{clean}')
        i += 1

print(f'\n{end_col}Fim do programa.{clean}\n')