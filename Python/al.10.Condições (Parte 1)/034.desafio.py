sal_in = float(input('Digite o seu salário: R$'))
if sal_in > 1250:
    sal_nv = sal_in*1.1
else:
    sal_nv = sal_in*1.15

print('Seu novo salário é R${:.2f}'.format(sal_nv))