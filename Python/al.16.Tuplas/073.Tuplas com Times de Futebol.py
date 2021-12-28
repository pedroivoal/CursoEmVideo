from colors import *

title = color_underline_bold['cyan']
answer_col = color['blue']
clean = color['clean']

tit = f'{title}Tabela do Brasileirão{clean}'
print(f'\n{tit:^60}\n')

tabela = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Corinthians', 'Corinthians', 'América-MG', 'Atlético-GO', 'Santos', 'Ceará', 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense')

for i in range(0,5):
    print(f'{answer_col}{i+1}º colocado: {tabela[i]}{clean}')
print()
for i in range(len(tabela)-4, len(tabela)):
    print(f'{answer_col}{i+1}º colocado: {tabela[i]}{clean}')
print()

pc = tabela.find('chapecoense')
print(f'{answer_col}{tabela[pc]} está na {pc}ª posição.{clean}')
