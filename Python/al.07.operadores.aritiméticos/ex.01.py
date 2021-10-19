n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

soma = n1 + n2
subtr = n1 - n2
mult = n1 * n2
div = n1 / n2
pot = n1**n2  # pow(n1, n2)
div_int = n1 // n2
div_rest = n1 % n2

print('{} + {} = {}'.format(n1, n2, soma),)
print('{} - {} = {}'.format(n1, n2, subtr))
print('{} * {} = {}'.format(n1, n2, mult))
print('{} / {} = {}'.format(n1, n2, div))
print('{} ** {} = {}'.format(n1, n2, pot))
print('{} // {} = {}'.format(n1, n2, div_int))
print('{} % {} = {}'.format(n1, n2, div_rest))

# end = ' bunda ' >>> substitui o pulo de linha automatico no final do print()
# \n >>> pula linha