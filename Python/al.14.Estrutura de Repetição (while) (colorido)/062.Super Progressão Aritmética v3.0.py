from colors import color, color_underline_bold

# cores para texto 
title = color_underline_bold['cyan']
answer_col = color['blue']
error_col = color['red']
end_col = color['purple']
clean = color['clean']

print('\n{}----10 primeiros valores de uma PA----{}\n'.format(title, clean))
a1 = float(input('Digite o 1º termo: '))
r = float(input('Digite a razão: '))
rp = '(' + str(a1)
nt = 0

i = 1
while i < 10:

    rp += ', {}'.format(r*i+ a1)

    i += 1

nt = i
a1 = r*(i)+ a1
rp += ', ...)'

print('\n{1}{0}{2}\n'.format(rp, answer_col, clean))

n = int(input('Digete quantos termos a mais deseja ver: '))

while n != 0:

    rp = '(...' + str(a1)

    i = 1
    while i < n:

        rp += ', {}'.format(r*i+ a1)

        i += 1

    nt += i
    a1 = r*(i)+ a1
    rp += '...)'

    print('\n{1}{0}{2}\n'.format(rp, answer_col, clean))

    n = int(input('Digete quantos termos a mais deseja ver: '))

    print('\n{1} Foram exibidos {0} termos da PA.{2}'.format(nt, answer_col, clean))
print('\n{0}Fim do programa{1}\n'.format(end_col, clean))