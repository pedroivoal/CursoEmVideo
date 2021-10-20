filme = {}
filme['título'] = 'Star Wars'
filme['ano'] = 1977
filme['diretor'] = 'George Lucas'

print('values:', filme.values())
print('key:', filme.keys())
print('items:', filme.items())

for k,v in filme.items():
    print(f'O {k} é {v}')
