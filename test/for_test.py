
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

