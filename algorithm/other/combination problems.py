'''
N个鸡蛋放到M个篮子中，篮子不能为空，要满足：对任意不大于N的数量，能用若干个篮子中鸡蛋的和表示。

写出函数，对输入整数N和M，输出所有可能的鸡蛋的放法。
M = 2
N = 3
1 2
2 1

'''

def helper(egg_n, hamper_n, temp, res):
    if hamper_n == 1 and egg_n > 0:
        res.append(temp[:]+[egg_n])
        return
    if egg_n < 1:
        return


    for i in range(1, egg_n):
        temp.append(i)
        helper(egg_n-i, hamper_n-1, temp, res)
        temp.pop()

def combi_num(M, N):
    if M > N:
        return []
    res = []
    helper(N, M, [], res)
    return res

def all_fac(primes):
    def dfs(i, cur):
        if i == len(primes):
            print(cur)
            return
        dfs(i+1, cur)
        dfs(i+1, cur*primes[i])

    dfs(0, 1)

def all_fac2(primes, level, num):
    if level == 3:
        print(num)
        return
    for i in range(2):
        if i==1:
            num *= primes[level]
        all_fac2(primes, level+1, num)

# all_fac([2,3,7])
# print('------------********-----------')
# all_fac2([2,3,7], 0, 1)


print(combi_num(3,5))