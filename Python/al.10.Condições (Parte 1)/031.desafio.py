dist = float(input('Digite a distancia da viagem: '))

if dist <= 200:
    v = dist*0.5
else:
    v = dist*0.4

#v = dist*0.5 if dist <= 200 else v = dist*0.45

print('O preço da viagem é R${:.2f}'.format(v))

