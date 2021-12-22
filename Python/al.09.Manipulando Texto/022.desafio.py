nome = input('Digite seu nome: ').strip()

nome_up = nome.upper()
print(nome_up)

nome_low = nome.lower()
print(nome_low)

nome_sp = nome.split()
quant = len(nome) - nome.count(' ')

print(quant)
print(len(nome_sp[0]))