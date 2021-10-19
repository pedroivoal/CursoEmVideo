m = float(input('Digite um valor em metros: '))

mm = m*1000
cm = m*100
dm = m*10
m = m
dam = m/10
hm = m/100
km = m/1000

print('{} metro(s) = {} milimetro(s).'.format(m,mm))
print('{} metro(s) = {} centimetro(s).'.format(m, cm))
print('{} metro(s) = {} decimetro(s).'.format(m, dm))
print('')
print('{} metro(s) = {} decâmetro(s).'.format(m, dam))
print('{} metro(s) = {} hequitômetro(s).'.format(m, hm))
print('{} metro(s) = {} quilometro(s).'.format(m, km))
