
'''
0-n 之间， 二进制表示中，有多个bit 1,  0-5(101)共有7个
'''
def get_left_most2(n):
    m = 0
    while n > 1:
        n >>= 1
        m += 1
    return m

def get1bits(n):

    m = get_left_most2(n)

    if n == 0:
        return 0
    if n == (1 << m+1) - 1:
        return (m+1)*(1<<m)

    n = n - (1 << m)

    return n+1 + get1bits(n) + m*(1 << m-1)


# test = [1,2,3,4,5,6,7,8]
#
# print(get_left_most2(1))
# print(list(map(get1bits, test)))


'''
数一数在0到n之间有多少个数字k（0<=k<=9）。如n=12时，[0,1,2...,12]之间一共有5个1。分别包含在[1, 10, 11, 12]之中。
'''

#method1 recursive
def most_sig(n):
    '''

    :param n: positive int
    :return: most significant digit and number of digits
    '''
    m = 1
    while n > 9:
        m += 1
        n //= 10

    return (n,m)

def count_num(n,k):
    # not include 0
    if 0 <= n < 10:
        if k <= n:
            return 1
        else:
            return 0

    sig_d, num_d = most_sig(n)
    remain = n - sig_d*10**(num_d - 1)

    toAdd = sig_d*(num_d-1)*10**(num_d-2)
    if k == sig_d:
        toAdd += remain + 1
    elif k < sig_d:
        toAdd += 10**(num_d-1)

    return count_num(remain, k) + toAdd


#method2
def count_digit(n,k):
    digit_pos = 1
    curr_digit = n % 10
    res = 0
    remain = curr_digit
    if k <= curr_digit:
        res += 1
    n = n//10
    while n > 0:
        curr_digit = n % 10
        toAdd = curr_digit*digit_pos*10**(digit_pos-1)
        if k == curr_digit:
            toAdd += remain + 1
        elif k < curr_digit:
            toAdd += 10**(digit_pos)
        if n < 10 and k==0:
            while digit_pos >= 1:
                toAdd -= 10**digit_pos
                digit_pos -= 1
        res += toAdd
        remain = remain + curr_digit * 10**digit_pos
        digit_pos += 1
        n //= 10

    return res

# print(count_num(10,0))
print(count_digit(10,0))





