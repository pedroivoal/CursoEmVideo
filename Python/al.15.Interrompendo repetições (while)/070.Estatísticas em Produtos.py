from colors import color, color_underline_bold

title = color_underline_bold['cyan']
typed_col = color['green']
answer_col = color['blue']
error_col = color['red']
end_col = color['purple']
clean = color['clean']

print(f'\n{title}Leitor de preços{clean}\n')
Sum = 0
num_expensive_product = 0

name = input(f'Nome do produto: {typed_col}')
print(end = f'{clean}')
price = float(input(f'Preço do produto: {typed_col}'))
print(end = f'{clean}')

while True:
        i = input(f'Deseja continuar?[S/N] {typed_col}').strip().lower()
        print(end = f'{clean}')
        if i == 's' or i == 'n':
            break
        print(f'{error_col}Dados inválidos. Digite "S" ou "N".{clean}\n')

if price > 1000:
        num_expensive_product += 1

Sum += price
most_cheap_name = name
most_cheap_price = price

while True and i == 's':

    name = input(f'\nNome do produto: {typed_col}')
    print(end = f'{clean}')
    price = float(input(f'Preço do produto: {typed_col}'))
    print(end = f'{clean}')

    Sum += price

    if price > 1000:
        num_expensive_product += 1

    if price < most_cheap_price:
        most_cheap_name = name
        most_cheap_price = price

    while True:
        i = input(f'Deseja continuar?[S/N] {typed_col}').strip().lower()
        print(end = f'{clean}')
        if i == 's' or i == 'n':
            break
        print(f'{error_col}Dados inválidos. Digite "S" ou "N".{clean}\n')
    
    if i == 'n':
        break


print(f'\n{answer_col}Gastos totais: {Sum}')
print(f'Total de produtos que custavam mais que 1000 R$: {num_expensive_product}')
print(f'Produto mais barato: {most_cheap_name}, que custou {most_cheap_price} R$.{clean}')
print(f'\n{end_col}Fim do programa{clean}\n')