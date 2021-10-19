num = int(input('Digite um número: '))

u = num % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000
'''
m = num//1000
c = (num - m*1000)//100
d = (num - m*1000 - c*100)//10
u = (num - m*1000 - c*100 - d*10)//1'''

print('''Unidade(s): {}
Dezena(s): {}
Centena(s): {}
milhare(s): {}'''.format(u, d, c, m))

