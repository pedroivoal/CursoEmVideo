from colors import color, color_underline_bold

# cores para texto 
title = color_underline_bold['cyan']
answer_col = color['blue']
error_col = color['red']
end_col = color['purple']
clean = color['clean']

print('\n{}Digite vários números (inteiros){}\n'.format(title, clean))

num = int(input())
bigger = lower = num
c = 's'
Sum = i = 0


while c ==  's':

    Sum += num
    i += 1

    if num > bigger:
        bigger = num
    elif num < lower:
        lower = num

    c = input('\nDeseja continuar?[s/n]').strip().lower()
    if c == 's':
        num = int(input())

med = Sum/i

print('\n{2}Média dos {1} valores digitados é {0}{3}'.format(med, i, answer_col, clean))
print('{1}Maior valor digitado é {0}{2}'.format(bigger, answer_col, clean))
print('{1}Menor valor digitado é {0}{2}\n'.format(lower, answer_col, clean))