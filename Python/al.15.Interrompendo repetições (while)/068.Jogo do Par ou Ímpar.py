from colors import color, color_underline_bold
from random import randint

title = color_underline_bold['cyan']
typed_col = color['green']
answer_col = color['blue']
error_col = color['red']
end_col = color['purple']
clean = color['clean']

# Título
print(f'\n{title}Par ou Ímpar{clean}\n')

i = 0
# Loop principal
while True:

    move = input(f'Escolha, par[p] ou ímpar[i]: {typed_col}').strip().lower()
    print(end = f'{clean}')

    # Garante que valor digitado foi valido
    while move != 'p' and move != 'i':
        print(f'{error_col}Valor inválido.{clean}\n')
        move = input(f'Escolha, par[p] ou ímpar[i]: {typed_col}').strip().lower()
        print(end = f'{clean}')

    n = int(input(f'Digite um número: {typed_col}'))
    print(end = f'{clean}\n')

    n_pc = randint(0,5)

    print(f'Sua jogada: {n}')
    print(f'Jogada do PC: {n_pc}')

    # Verifica vencedor
    if (n + n_pc) % 2 == 0 and move == 'p':
        print(f'\n{answer_col}Você venceu.{clean}\n')
        i += 1
    elif (n + n_pc) % 2 == 1 and move == 'i':
        print(f'\n{answer_col}Você venceu.{clean}\n')
        i += 1
    else:
        print(f'\n{error_col}Você perdeu.{clean}\n')
        break

# Resutados finais
print(f'{answer_col}Você venceu {i} veze(s) seguida(s) antes de perder.{clean}')
print(f'\n{end_col}Fim do programa.{clean}\n')
