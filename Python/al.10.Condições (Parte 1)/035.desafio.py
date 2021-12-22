l1 = float(input('Digite o 1° lado do triângulo: '))
l2 = float(input('Digite o 2° lado do triângulo: '))
l3 = float(input('Digite o 3° lado do triângulo: '))

s3 = l1 + l2
s2 = l1 + l3
s1 = l2 + l3

if l3 >= s3 or l2 >= s2 or l1 >= s1:
    print('Não há triângulo com esses lados.')
else:
    print('Há triângulo com esses lados.')