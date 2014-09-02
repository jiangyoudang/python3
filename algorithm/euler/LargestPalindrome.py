# -*- coding utf-8 -*-
import itertools
from time import time

def is_palindrome(num):
    s = str(num)
    if s == s[::-1]:
        return True
    return False


def largestPalindrome(n):
    max_palindrome = 1
    for x in range(n,1,-1):
        if x*n < max_palindrome:
            break
        for y in range(n,x-1,-1):
            if is_palindrome(x*y) and x*y > max_palindrome:
                max_palindrome = x*y
            elif x*y < max_palindrome:          # 100 times efficiency improved
                break
    return max_palindrome

def lp2(n):
    return  max(x*y for x,y in itertools.product(range(n),repeat=2) if is_palindrome(x*y))


t0 = time()
print(lp2(999))
t1 = time()
print(largestPalindrome(999))
t2 = time()
print('Time cost: {} vs {}'.format(t1-t0,t2-t1))

