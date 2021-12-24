from colors import color, color_underline_bold

# cores para texto
title = color_underline_bold['cyan']
answer_col = color['blue']
error_col = color['red']
clean = color['clean']

print('\n{}Cálculo de Fatorial{}\n'.format(title, clean))
num = int(input('Digite um número inteiro (Maior ou igual a 0): '))

while num < 0:
    print('{}Valor inválido.{}'.format(error_col, clean))
    print()
    num = int(input('Digite um número inteiro (Maior ou igual a 0): '))

factorial = num
fac_print = ''
fac_print += '{}'.format(num)

i = num-1
while i > 0:

    factorial *= i
    fac_print += ' x {}'.format(i)

    i -= 1

print('\n{3}{0}! = {1} = {2}{4}\n'.format(num, fac_print, factorial, answer_col, clean))