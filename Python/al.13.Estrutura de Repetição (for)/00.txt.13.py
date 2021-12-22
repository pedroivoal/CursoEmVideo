v = 2
for c in range(2, 100, v):
    print(c, end = ', ')
    if c % 30 == 0:
        print()
print('{}.'.format(c + v))