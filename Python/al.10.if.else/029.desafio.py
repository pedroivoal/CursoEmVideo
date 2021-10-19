vel = float(input('Digite a velocidade do carro: '))
if vel > 80:
    i = 0
    print('Você foi multado.')
    i = 7 * (vel - 80)
    print('Valor da multa: R${:.2f}'.format(i))
