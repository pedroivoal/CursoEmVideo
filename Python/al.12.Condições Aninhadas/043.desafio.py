def faixa_IMC(peso, altura):

    IMC = peso/(altura/100)**2

    if IMC < 18.5:
        faixa = 'Abaixo do peso'
    elif IMC < 25:
        faixa = 'Peso ideal'
    elif IMC < 30:
        faixa = 'Sobrepeso'
    elif IMC < 40:
        faixa = 'Obesidade'
    else:
        faixa = 'Obesidade Mórbida'

    return faixa

alt = int(input('Digite sua altura em cm: '))
peso = float(input('Digite seu peso em kg: '))
faixa = faixa_IMC(peso, alt)
print('{}'.format(faixa))
