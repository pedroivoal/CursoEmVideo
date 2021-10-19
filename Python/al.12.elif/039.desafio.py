from datetime import date

ano_at = date.today().year
ano_nasc = int(input('Digite o ano em que você nasceu: '))

#a idade até o fim do ano
idade = ano_at - ano_nasc

if idade < 18:
    print('\nVocê vai se alistar daqui a {} anos.'.format(18-idade))
elif idade == 18:
    print('\nÉ hora de se alistar.')
else:
    print('\nJá passou o tempo de se alistar há {} anos'.format(idade-18))