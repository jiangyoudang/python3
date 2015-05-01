
'''
Given n items with size A[i], an integer m denotes the size of a backpack. How full you can fill this backpack?
If we have 4 items with size [2, 3, 5, 7], the backpack size is 11, we can select 2, 3 and 5,
so that the max size we can fill this backpack is 10. If the backpack size is 12.
we can select [2, 3, 7] so that we can fulfill the backpack.

You function should return the max size we can fill in the given backpack.
'''
def knapsack(m, A):
    if not A:
        return 0
    n = len(A)
    A.sort()
    pack = [0]
    res = A[0]
    sum = A[0]
    while pack:
        if sum <= m:
            res = max(res,sum)
            print([A[i] for i in pack], sum)
            if pack[-1] < n-1:
                pack.append(pack[-1] + 1)
                sum += A[pack[-1]]
                continue
        i = pack.pop()
        if not pack:
            break
        sum -= A[i]
        sum -= A[pack[-1]]
        next_i = pack[-1] + 1
        #remove duplicate
        while A[next_i] == A[next_i-1]:
            next_i += 1
            if next_i == n:
                i = pack.pop()
                sum -= A[i]
                if not pack:
                    return res
                next_i = pack[-1] + 1

        pack[-1] = next_i
        sum += A[pack[-1]]

    return res

def helper(m, A, temp, res):
    if m < 0:
        print(temp, sum(temp))
        return
    else:
        print(temp, sum(temp))
        res[0] = max(res[0], sum(temp))
        if not A:
            return

    for i,num in enumerate(A):
        if i > 0 and num == A[i-1]:
            continue
        if num > m:
            break
        temp.append(num)
        helper(m-num, A[i+1:], temp, res)
        temp.pop()


def knapsack_r(m, A):
    A.sort()
    res = [A[0]]
    helper(m, A, [], res)
    return res[0]



'''
Given n items with size A[i] and value V[i], and a backpack with size m. What's the maximum value can you put into the backpack?
'''
def knapsack_value_helper(m, A, V, temp, res, curr_value):

    if m  > 0:
        res[0] = max(res[0], curr_value)
    if not A:
        return

    i = 0
    if temp:
        i = temp[-1] + 1
    while i < len(A) and m > A[i]:
        temp.append(i)
        curr_value += V[i]
        knapsack_value_helper(m-A[i], A,V, temp, res, curr_value)
        curr_value -= V[i]
        temp.pop()
        i += 1


def knapsack_Value(m, A, V):
    res = [0]
    knapsack_value_helper(m, A, V, [], res, 0)
    return res[0]


# dp
def knapsack_value_dp(m,A,V):
    dp = [float('-inf')] * (m+1)
    temp = set()
    for i, size in enumerate(A):
        value = V[i]
        if size > m:
            continue
        dp_temp = dp[:]
        for pre in temp.copy():

            if size+pre < m+1:
                temp.add(size+pre)
                dp[size+pre] = max(dp_temp[size+pre], value+dp_temp[pre])
        dp[size] = max(dp[size], value)
        temp.add(size)
    return max(dp)

'''
dp2 : dp[i][w] = max(dp[i-1][w-wi] + V[i], dp[i-1][w], wi < w)
'''
def knapsack_value_dp2(m, A, V):
    A_length = len(A)
    dp = [[0] * (m+1) for j in range(A_length+1)]

    for i in range(1, A_length+1):
        for w in range(m+1):
            wi = A[i-1]
            if wi <= w:
                dp[i][w] = max(dp[i-1][w-wi] + V[i-1], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    #output the items
    res = []
    w = m
    for i in range(A_length,0,-1):
        if dp[i][w] != dp[i-1][w]:
            res.append((i, A[i-1]))
            w -= A[i-1]
    print(res)


    return dp[A_length][m]






m = 300
# A = [12,3,7,4,5,13,2,8,4,7,6,5,7]
# A = [2,3,5,7]
# V = [1,5,2,4]
A = [71,34,82,23,1,88,12,57,10,68,5,33,37,69,98,24,26,83,16,26,18,43,52,71,22,65,68,8,40,40,24,72,16,34,10,19,28,13,34,98,29,31,79,33,60,74,44,56,54,17,63,83,100,54,10,5,79,42,65,93,52,64,85,68,54,62,29,40,35,90,47,77,87,75,39,18,38,25,61,13,36,53,46,28,44,34,39,69,42,97,34,83,8,74,38,74,22,40,7,94]
V = [26,59,30,19,66,85,94,8,3,44,5,1,41,82,76,1,12,81,73,32,74,54,62,41,19,10,65,53,56,53,70,66,58,22,72,33,96,88,68,45,44,61,78,78,6,66,11,59,83,48,52,7,51,37,89,72,23,52,55,44,57,45,11,90,31,38,48,75,56,64,73,66,35,50,16,51,33,58,85,77,71,87,69,52,10,13,39,75,38,13,90,35,83,93,61,62,95,73,26,85]
# A = [95,75,23,73,50,22,6,57,89,98]
# V = [89,59,19,43,100,72,44,16,7,64]
# temp = sorted([(A[i], V[i]) for i in range(len(A))])
# A = []
# V = []
# for t in temp:
#     a, v = t
#     A.append(a)
#     V.append(v)
# A = [1,2,2,3]
# print(knapsack(m, A))
# print('-----------')
# print(knapsack_r(m, A))
# print(knapsack_Value(m, A, V))
print(knapsack_value_dp(m, A, V))
print(knapsack_value_dp2(m, A, V))

def comb_sum_helper(nums, target, temp, res):
    if target == 0 :
        res.append(temp[:])
        return

    for num in nums:
        if not temp or temp and temp[-1] <= num:
            if target < num:
                break
            temp.append(num)
            comb_sum_helper(nums, target-num, temp, res)
            temp.pop()



def comb_sum(nums, target):
    nums = list(set(nums))
    nums.sort()
    res = []
    comb_sum_helper(nums, target, [], res)
    return res

# print(comb_sum(A, m))


# NOT GOOD
def combinationSum(candidates, target):
        candidates.sort()
        stack = [candidates[0]]
        curr_total = sum(stack)
        res = []
        while stack:
            if curr_total < target:
                stack.append(stack[-1])
                curr_total += stack[-1]

            elif curr_total >= target:
                if curr_total == target:
                    res.append(stack[:])
                curr_total -= stack[-1]
                stack.pop()
                if not stack:
                    break
                next_index = candidates.index(stack[-1]) + 1
                while next_index == len(candidates):
                    curr_total -= stack.pop()
                    if not stack:
                        break
                    next_index = candidates.index(stack[-1]) + 1

                else:
                    stack[-1] = candidates[next_index]
                    curr_total += stack[-1] - candidates[next_index-1]

        return res
def combinationSum2(candidates, target):
    dp = {}
    for i in range(1, target+1):
        for j in candidates:
            curr = i-j
            if curr == 0:
                dp[i] = [i]
            elif curr > 0:
                if curr >=j and curr in dp:
                    dp[i] = dp.get(curr, [])[:]
    return dp


def perm(temp, avail, res):

    if len(avail) == 1:
        res.append((temp+avail)[:])
        return

    for e in avail[:]:
        temp.append(e)
        avail.remove(e)
        perm(temp, avail, res)
        avail.append(temp.pop())


