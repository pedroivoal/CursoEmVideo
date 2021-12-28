from colors import *

title = color_underline_bold['cyan']
typed_col = color['green']
answer_col = color['blue']
error_col = color_underline['red']
clean = color['clean']

extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
t = f'{title}Número por extenso{clean}'
print('{:^100}\n'.format(t))

while True:
    num = input(f'Digite um número entre 0 e 20: {typed_col}')
    print(end = f'{clean}')
    n = num.isnumeric()
    if n:
        num = int(num)
        if num in range(0, 21):
            break
    print(f'{error_col}Dados inválidos. Digite um número entre 0 e 20{clean}\n')

print(f'\n{answer_col}{num} = {extenso[num]}{clean}\n')