lower = 0
bigger = 0

for i in range(0, 5):

    weithg = float(input('Digite {}º peso: '.format(i+1)))

    if i == 0:
        bigger = weithg
        lower = weithg

    if weithg > bigger:
        bigger = weithg
    elif weithg < lower:
        lower = weithg
    
print('Menor peso: {}'.format(lower))
print('Maior peso: {}'.format(bigger))