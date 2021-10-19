import math

num = float(input('Digite um número: '))

res = math.floor(num)
#res = math.trunc(num)
#res = num//1
#res = int(num)


print('O número {} tem parte inteira {}.'.format(num, res))