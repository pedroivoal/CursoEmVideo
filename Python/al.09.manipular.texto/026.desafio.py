frase = input('Digite uma frase: ').strip()

frase = frase.lower()
na = frase.count('a')
ap1 = frase.find('a') + 1
apn = frase.rfind('a') + 1

print('''
A letra 'a': 
Aparece: {} vezes.
1° na psição: {}.
Por último na posição: {}.'''.format(na, ap1, apn))
