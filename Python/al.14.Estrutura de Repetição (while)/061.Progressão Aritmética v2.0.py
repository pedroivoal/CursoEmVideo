from colors import color, color_underline

title = color_underline['green']
answer_col = color['blue']
clean = color['clean']

print('\n{}----10 primeiros valores de uma PA----{}\n'.format(title, clean))
a1 = float(input('Digite o 1º termo: '))
r = float(input('Digite a razão: '))
rp = '(' + str(a1)

i = 1
while i < 10:

    rp += ', {}'.format(r*i+ a1)

    i += 1

rp += ')'

print('\n{1}{0}{2}\n'.format(rp, answer_col, clean))