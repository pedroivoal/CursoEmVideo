frase = 'Curso em Vídeo Python'
print('(0)',frase,'\n')

# printa 16° letra
print('(1)',frase[15],'\n')

#printa da [10° à 13°]
print('(2)',frase[9:13],'\n')

#printa da [10° à 21°(últma)]
print('(3)',frase[9:21])
print('(3)',frase[9:],'\n')

#printa da [10° à 21°(últma)] "andando" de 2 em 2 casas
print('(4)',frase[9:21:2])
print('(4)',frase[9::2],'\n')

#printa da 1° à 5°
print('(5)',frase[:5],'\n')

#devolve o tamanho da lista
len = len(frase)
print('(6)',len, '\n')

#conta o número de aparições de algo
count_o1 = frase.count('o')
count_cu = frase.count('Cu')
count_o2 = frase.count('o',0,14)
print('(7)',count_o1)
print('(7)',count_cu)
print('(7)',count_o2, '\n')

#mostra primeira aparição de algo
find_o = frase.find('o')
find_deo = frase.find('deo')
find_in = frase.find('in')
print('(8)',find_o)
print('(8)',find_deo)
print('(8)',find_in, '\n')

#troca um elemento da string por outro
frase_nova = frase.replace('Python', 'Android')
print('(9)',frase_nova, '\n')

#deixa todas letras maiúculas,minúculas, etc
frase_up  = frase.upper()
frase_low = frase.lower()
frase_cap = frase.capitalize()
frase_tit = frase.title()
print('(10)', frase_up)
print('(10)', frase_low)
print('(10)', frase_cap)
print('(10)', frase_tit, '\n')

frase = '   Aprenda Python  '
print('(0)',frase,'\n')

# remove espaços inúteis
frase_st = frase.strip()
frase_rst = frase.rstrip()
frase_lst = frase.lstrip()
print('(11)', frase_st)
print('(11)', frase_rst)
print('(11)', frase_lst, '\n')

frase = 'Curso em Vídeo Python'
print('(0)',frase,'\n')

# cria uma lista comcada palavra
frase_sp  = frase.split()
print('(12)', frase_sp, '\n')

#põe um simbolo entre elemetos da lista
frase_jo = '_'.join(frase)
frase_sp_jo = '_'.join(frase_sp)
print('(13)', frase_jo)
print('(13)', frase_sp_jo, '\n')

#como 'misturar' módulos
frase_up_E = frase.upper().count('E')
print(frase_up_E)