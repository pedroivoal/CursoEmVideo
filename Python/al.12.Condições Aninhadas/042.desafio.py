def tipo_triangulo(l1, l2, l3):
    if l1==l2 and l2==l3:
        triangulo = 'Equilátero'
    elif l1!=l2 and l1!=l3 and l2!=l3:
        triangulo = 'Escaleno'
    else:
        triangulo = 'Isóceles'

    return triangulo 

l1 = float(input('Digite o 1° lado do triângulo: '))
l2 = float(input('Digite o 2° lado do triângulo: '))
l3 = float(input('Digite o 3° lado do triângulo: '))

s3 = l1 + l2
s2 = l1 + l3
s1 = l2 + l3

if l3 >= s3 or l2 >= s2 or l1 >= s1:
    print('Não há triângulo com esses lados.')
else:
    tipo = tipo_triangulo(l1, l2, l3)
    print('Triangulo do tipo {}'.format(tipo))