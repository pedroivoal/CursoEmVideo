cidade = input('Digite o nome de uma cidade: ')
cidade_sp = cidade.split()

print('O nome da cidade começa com Santo. ',  end = '')

print(cidade_sp[0].upper() == 'SANTO')