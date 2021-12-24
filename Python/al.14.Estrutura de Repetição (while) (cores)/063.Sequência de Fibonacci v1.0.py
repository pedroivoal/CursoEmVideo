from colors import color, color_underline_bold

# cores para texto 
title = color_underline_bold['cyan']
answer_col = color['blue']
error_col = color['red']
end_col = color['purple']
clean = color['clean']

print('\n{}Quantos números da Segquência de Fibonacci você deseja ver?{}\n'.format(title, clean))
n = int(input('Digite um número: '))

i = 0
tn1 = 0
tn2 = 1
sequence = '({}, {}'.format(tn1, tn2)
while i < n-2:
    tn3 = tn2 + tn1
    tn1 = tn2
    tn2 = tn3
    sequence += ', {}'.format(tn2)

    i += 1

sequence += ', ...)'

print('\n{1}Segquência de Fibonacci até o {0}º termo.{2}'.format(n, answer_col, clean))
print('{1}{0}{2}\n'.format(sequence, answer_col, clean))