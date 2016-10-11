import functools
import copy

def minus(f):
    @functools.wraps(f)
    def a(*args):
        return 'c'+f(*args)
    return a

@minus
def xxx(x):
    print('ok')
    return 'b'+ x


def partition(s):

    res = []
    temp = []

    def isPalindrome(s):
        return s==s[::-1]

    def partPalindrome(s, temp, res):
        if not s:
            res.append(temp[:])
        for i in range(len(s)):
            if isPalindrome(s[:i+1]):
                temp.append(s[:i+1])
                partPalindrome(s[i+1:], temp, res)
                temp.pop()
    partPalindrome(s, temp, res)
    return res
s = 'aab'
print(partition(s))