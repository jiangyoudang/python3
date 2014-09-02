__author__ = 'congliu'

# -*- coding utf-8 -*-

import math


def fibonacci(num):
    result_list = []
    a = 1
    b = 1
    while (b <= num):
        a, b = b, a + b
        result_list.append(a)
    return result_list


def is_prime(num):
    if num < 2:
        raise ValueError
    d = 2
    while d <= num / d:
        if num % d == 0:
            return False
        else:
            d += 1
    return True


def lgf(n):
    '''
    return Largest Prime Factor(LPF)
    '''
    d = 2
    while d < n / d:  # dynamic loop
        if n % d == 0:
            n /= d
        else:
            d += 1
    return n


def GCD(num1, num2):
    '''
    return the greatest common divisor of two integers
    '''
    while (num1 % num2):
        num1, num2 = num2, num1 % num2
    return num2


# def GCD_vector(*num):
#     if len(num) == 2:
#         return GCD(*num)
#     else:
#         return GCD(GCD_vector(*num[:-1]),num[-1])

def GCD_list(num):
    '''
    return the greatest common divisor of a list of integers
    '''
    if len(num) == 2:
        return GCD(*num)
    else:
        return GCD(GCD_list(num[:-1]), num[-1])

        # test

        # print(GCD_vector(20,50,30,60))

        #print(GCD_list([20,50,30,60]))
        #print(GCD_list((5,20)))