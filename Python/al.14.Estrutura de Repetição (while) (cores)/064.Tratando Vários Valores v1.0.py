from colors import color, color_underline_bold

# cores para texto 
title = color_underline_bold['cyan']
answer_col = color['blue']
error_col = color['red']
end_col = color['purple']
clean = color['clean']

print('\n{}Digite vários números (inteiros){}\n'.format(title, clean))
print('Para finalizar digite 999.')

num = int(input())

Sum = 0
i = 0
while num != 999:

    Sum += num
    i += 1
    num = int(input())


print('\n{1}Foram digitados {0} números.{2}'.format(i, answer_col, clean))
print('{1}A soma de todos eles é {0}.{2}\n'.format(Sum, answer_col, clean))