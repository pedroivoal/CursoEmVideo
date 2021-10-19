num = int(input('Digite um número: '))
c = 0
z = int(num**(1/2) +1)

for i in range(2, z):
    if num%i == 0:
        c += 1

    #if c == 1:
    #break

if c == 0 and num != 1:
    print('{} é primo.'.format(num))
else:
    print('{} não é primo'.format(num))