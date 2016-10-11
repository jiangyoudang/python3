class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        if len(num)<=1:
            return [num]
        pre_res = self.permute(num[1:])
        curr = [num[0]]
        res = []
        for i in range(len(pre_res[0])+1):
            for pre in pre_res:
                res.append(pre[:i]+curr+pre[i:])
        return res
def permute2(num):
    if len(num)==0:
        return num
    pre_res = [[num[0]]]
    for curr in num[1:]:
        res = []
        for i in range(len(pre_res[0])+1):
            for pre in pre_res:
                res.append(pre[:i]+[curr]+pre[i:])
        pre_res = res
    return pre_res

#根据定义
def permute3(num, permutation, res):
    if not num:
        res.append(permutation[:])
        return

    for i in range(len(num)):
        if i>0 and num[i]==num[i-1]:
            continue
        permutation.append(num[i])
        permute3(num[:i]+num[i+1:], permutation, res)
        permutation.pop()


test_case = [1,2,3,1]
# res = Solution().permute(test_case)
# res = permute2(test_case)
res= []
permute3(sorted(test_case), [], res)
print(res)
