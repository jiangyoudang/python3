
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


test = [1,2,3,4,5,6,7,8]

print(get_left_most2(1))
print(list(map(get1bits, test)))

