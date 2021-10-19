dia = int(input('Digite o número de dias de uso do carro: '))
km = float(input('Digite o total de km rodados: '))

prec = 60*dia + 0.15*km

print('O preço a pagar é {:.2f} reais.'.format(prec))