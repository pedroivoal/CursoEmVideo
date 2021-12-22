nome = input('Digite seu nome: ')
nome_up_sp = nome.upper().split()

if nome_up_sp[0] == 'PEDRO':
    print('Seu 1° nome é o mais bonito.')
elif nome_up_sp[0] == 'TAINÁ' or nome_up_sp[0] == 'TAINA':
    print('Seu 1° nome é o mesmo que o da mulher mais bonita.')
else:
    print('Seu nome é bonito.')

print('Tenha um bom dia {}.'.format(nome))