num = int(input('Digite o número da tabuada: '))

for i in range(1, 11):
    print('{} x {} = {}'.format(i, num, num*i))