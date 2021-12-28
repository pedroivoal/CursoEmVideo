from colors import *
from random import randint

tup = [randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10)]
tup = tuple(tup)
print(tup)

for i in range(0, 5):
    if i == 0:
        maxi = tup[i]
    if tup[i] > maxi:
        maxi = tup[i]
print(maxi)

for i in range(0, 5):
    if i == 0:
        mani = tup[i]
    if tup[i] < mani:
        mani = tup[i]
print(mani)