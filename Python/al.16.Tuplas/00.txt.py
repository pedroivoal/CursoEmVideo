lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata')

print(lanche, '\n')

for i in lanche:
    print(f'Eu vou comer {i}')
print()

for i in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[i]}')
print()

for pos, element in enumerate(lanche):
    print(f'Eu vou comer {element}, da posição {pos}.')
print()

print(sorted(lanche))

a = (1, 2)
b = (3, 4)
ab = a + b
ba = b + a
print(a)
print(b)
print(ab)
print(ba)

# L = lista qualquer
# L.count('something')
# L.index('something')
# L.find('something')
# del(L)
# sorted(L)
# len(L)