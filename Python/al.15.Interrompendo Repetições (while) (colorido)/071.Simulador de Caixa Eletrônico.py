from colors import color, color_underline_bold

title = color_underline_bold['cyan']
typed_col = color['green']
answer_col = color['blue']
error_col = color['red']
end_col = color['purple']
clean = color['clean']

print(f'\n{title}Caixa eletrônico{clean}\n')

value = int(input(f'Digite o valor que deseja sacar: {typed_col}'))
print(end = f'{clean}\n')

n50 = value//50
value -= n50*50
n20 = value//20
value -= n20*20
n10 = value//10
value -= n10*10
n1 = value//1

print(f'''{answer_col}
Cédulas a serem entregues
Cédulas 50: {n50}
Cédulas 20: {n20}
Cédulas 10: {n10}
Cédulas 1: {n1}
''')