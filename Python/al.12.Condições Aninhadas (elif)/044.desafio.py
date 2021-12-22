def valor(value, type):

    if type == 'cheque' or 'dinheiro':
        final_v = value*0.9
    elif type == 'cartao' or type == 'cartão':
        final_v = value*0.95
    elif type == '2x cartao' or type == '2x cartão':
        final_v = value
    else:
        final_v = value*1.2
    
    return final_v

val = float(input('Digite o preço: '))
type = input('Digite a forma de pagamento: ').lower().strip()
print('Valor final do produto: {}'.format(valor(val, type)))

