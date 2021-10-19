import datetime

print('0 retorna ano atual.')
ano = int(input('Digite o ano: '))

if ano ==0:
    ano = datetime.date.today().year

# alternativa para o código abaixo
'''if ano%4 == 0:
    if ano%100 == 0:
        if ano%400 == 0:
            print('{} é bissexto.'.format(ano))
        else:
            print('{} não é bissexto.'.format(ano))
    else:
        print('{} é bissexto'.format(ano))
else:
    print('{} não é bissexto.'.format(ano))'''

if ano%4 == 0 and ano%100 != 0 or ano%400 == 0:
    bi = True
else:
    bi = False