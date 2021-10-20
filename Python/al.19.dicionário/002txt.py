pessoas = {
    'nome':'Pedro Ivo',
    'sexo':'M',
    'idade':18,
}
print(f'\nO {pessoas["nome"]} tem {pessoas["idade"]} anos.\n')
print(pessoas.keys(),'\n') 

for k in pessoas.keys():
    print(f'key: {k}')
print()

for v in pessoas.values():
    print(f'value: {v}')
print()

for k,v in pessoas.items():
    print(f'key: {k} --- value: {v}')
print()