s = 'abcdef'

# capitalize permutation

def perm_(s):
    temp = list(s)
    res = []
    n = len(temp)
    for i in range(1, 1<<n):
        for j in range(n):
            if temp[j] == s[j]:
                temp[j] = s[j].upper()
                res.append(''.join(temp))
                break
            else:
                temp[j] = s[j]

    return res


print(perm_(s))