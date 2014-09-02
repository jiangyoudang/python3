__author__ = 'congliu'

import math
import time
from algorithm.euler import numAl


#print(largest_prime_factors(600851475143))

t= time.time()

n=600851475143

def lgf(n):
    d=2
    while d < n/d:          # dynamic loop
        if n%d==0:
            n/=d
        else:
            d+=1
    return n

print(lgf(n))
print(time.time()-t)
