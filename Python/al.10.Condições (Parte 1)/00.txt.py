'''nome = input('Digite seu nome: ').title()
# os c[odigos abaixo funcionam da mesma forma
if nome == 'Gustavo':
    print('Que nome de viado.')
else:
    print('Que nome lindo.')

print('Que nome de viado.'if nome == 'Gustavo' else 'Que nome lindo.')'''

n1 = float(input('Digite a 1° nota: '))
n2 = float(input('Digite a 2° nota: '))
m = (n1 + n2)/2
print('Média: {}'.format(m))
print('Passou.' if m >= 6 else 'Reprovou.')