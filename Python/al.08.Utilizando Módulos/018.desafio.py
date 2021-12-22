import math

ang_graus =float(input('Digite um ânugulo em graus: '))

ang_rad = math.radians(ang_graus)
tg = math.tan(ang_rad)
sen = math.sin(ang_rad)
cos = math.cos(ang_rad)

print('Ângulo: {}'.format(ang_graus))
print('Seno: {:.2f}'.format(sen))
print('Cosseno: {:.2f}'.format(cos))
print('Tangente: {:.2f}'.format(tg))
