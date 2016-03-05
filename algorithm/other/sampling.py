
'''
sampling algorithm
'''

from random import randint, seed

n = 10
m = 3

i = 0

while i < n:
    ra = randint(100,99999)
    if ra%(n-i) < m:
        print(i)
        m -= 1
    if m==0 :
        break

    i += 1

