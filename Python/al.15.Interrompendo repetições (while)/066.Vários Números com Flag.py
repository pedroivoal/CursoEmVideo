from colors import color, color_underline_bold

title = color_underline_bold['cyan']
typed_col = color['green']
answer_col = color['blue']
clean = color['clean']

print(f'\n{title}Contador e Somador de Números{clean}\n')
print('Digite 999 para finalizar o programa\n')

Sum = 0
i = 0
while True:

    n = float(input(f'Digite um número: {typed_col}'))
    print(end = f'{clean}')

    if n == 999:
        break

    Sum += n
    i += 1

print(f'\n{answer_col}Soma dos valores digitados: {Sum}{clean}')
print(f'{answer_col}Número de valores digitados: {i}{clean}\n')
