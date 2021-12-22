frase = input('Digite uma frase: ').strip().upper()
s1 = [0]*(len(frase) - frase.count(' '))
s2 = [0]*(len(frase) - frase.count(' '))
c1 = 0
c2 = 0

for i in range(0, len(frase)):
    if frase[i] != ' ':
        s1[c1] = frase[i]
        c1 += 1

for i in range(len(frase)-1, -1, -1):
    if frase[i] != ' ':
        s2[c2] = frase[i]
        c2 += 1

if s1 == s2:
    print('Palindromo.')
else:
    print('Não palindromo.')