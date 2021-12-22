'''import  math

c1 = float(input('Digite o valor de um cateto: '))
c2 =float(input('Digite o valor de outro cateto: '))

hip = math.sqrt(c1**2 + c2**2)

print('Hipoternusa={}'.format(hip))'''

'''c1 = float(input('Digite o valor de um cateto: '))
c2 =float(input('Digite o valor de outro cateto: '))

hip = (c1**2 + c2**2)**(1/2)

print('Hipoternusa = {}'.format(hip))'''

from math import hypot

c1 = float(input('Digite o valor de um cateto: '))
c2 =float(input('Digite o valor de outro cateto: '))

hip = hypot(c1, c2)

print('Hipoternusa={:.4f}'.format(hip))