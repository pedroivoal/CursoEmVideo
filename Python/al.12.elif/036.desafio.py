prec_casa = float(input('Digite o valor da casa: '))
salar = float(input('Digite seu salário: '))
anos = int(input('Digite em quantos anos quitará o empréstimo: '))
parcela = prec_casa/(anos*12)
print()

if parcela > 0.3*salar:
    print('Desculpe, a parcela deve ser menor que 30% do salário.')
else:
    print('''Empréstimo aprovado.
Parcela mensal: R${}
Número de parcelas: {}'''.format(parcela, anos*12))