nome = input('Digite seu nome: ').title()

nome_sp = nome.split()

print('Primeiro nome: {}'.format(nome_sp[0]))
print('Último nome: {}'.format(nome_sp[len(nome_sp)-1]) )
