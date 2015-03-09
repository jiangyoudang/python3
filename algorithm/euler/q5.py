__author__ = 'congliu'

import time
from algorithm.euler import numAl

# q5: smallest multiple
def smulti(nums):
    dict_primes = {}
    for i in nums:
        prime_list = get_primes(i)
        for j in prime_list:
            if dict_primes.get(j, 0) < prime_list.count(j):
                dict_primes[j] = prime_list.count(j)
    result = 1
    for item in dict_primes.items():
        result *= item[0] ** item[1]
    return result


def get_primes(n):
    if n < 1:
        raise ValueError
    primes = []
    d = 2
    while d <= n / d:
        if n % d == 0:
            primes.append(d)
            n /= d
        else:
            d += 1
    primes.append(n)
    return primes

#q6: sum square difference
def sum_sq_di(nums):
    result = 0
    li = list(nums)
    while li:
        curr = li.pop()
        for i in li:
            result += 2*i*curr
    return result

#q7: 10001st prime
def get_prime(i):
    count = 0
    num = 1
    while count<i:
        num += 1
        if numAl.is_prime(num):
            count += 1

    return num

time0 = time.time()

# print(smulti(range(1, 20)))
# print(sum_sq_di(range(1,11)))
print(get_prime(10001))
print(get_primes(10))
time1 = time.time()

print(time1 - time0)