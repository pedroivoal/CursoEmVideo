lower = -1
bigger = 0

for i in range(0, 5):

    weithg = float(input('Digite o peso: '))

    if lower == -1:
        bigger = weithg
        lower = weithg

    if weithg > bigger:
        bigger = weithg
    elif weithg < lower:
        lower = weithg
    
print('Menor peso: {}'.format(lower))
print('Maior peso: {}'.format(bigger))