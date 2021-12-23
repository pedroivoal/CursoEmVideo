from colors import color

answer_col = color['purple']
clean = color['clean']

num = int(input('\nDigite um número inteiro (Maior ou igual a 0): '))

factorial = 1
i = 1
fac_print = ''
fac_print += '{}'.format(i)
i += 1

while i <= num:

    factorial = factorial*i
    fac_print += ' x {}'.format(i)

    i += 1

print('\n{3}{0}! = {1} = {2}{4}\n'.format(num, fac_print, factorial, answer_col, clean))