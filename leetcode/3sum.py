import time
class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        num.sort()
        pos_i = 0
        res = set()
        for i in num:
            if i>=0:
                break
            pos_i += 1
        if pos_i==len(num):
            return []

        for i in range(pos_i):
            j = i+1
            k = len(num)-1
            if i>0 and num[i]==num[i-1]:
                continue
            while k>=pos_i and j<k:
                tmp = (num[i],num[j],num[k])
                s = sum(tmp)
                if s>0:
                    k -= 1
                elif s<0:
                    j += 1
                else:
                    res.add(tmp)
                    j += 1
                    k -= 1
        # special case: (0,0,0)
        if num[pos_i]==0:
            if len(num)-pos_i>=3 and num[pos_i+1]==0 and num[pos_i+2]==0:
                res.add((0,0,0))
        # result = [list(t) for t in res]


        return map(list, res)
        # return sorted(result, key= lambda x:x[0])

t1 = time.time()
test = Solution()
a = [7,-1,14,-12,-8,7,2,-15,8,8,-8,-14,-4,-5,7,9,11,-4,-15,-6,1,-14,4,
     3,10,-5,2,1,6,11,2,-2,-5,-7,-6,2,-15,11,-6,8,-4,2,1,-1,4,-6,-15,1,
     5,-15,10,14,9,-8,-6,4,-6,11,12,-15,7,-1,-9,9,-1,0,-4,-1,-12,-2,14,
     -9,7,0,-3,-4,1,-2,12,14,-10,0,5,14,-1,14,3,8,10,-8,8,-5,-2,6,-11,
     12,13,-7,-12,8,6,-13,14,-2,-5,-11,1,3,-6]
a = [6,-5,-6,-1,-2,8,-1,4,-10,-8,-10,-2,-4,-1,-8,-2,8,9,-5,-2,-8,-9,-3,-5]
a = [-1,-3,4]
res = test.threeSum(a)
for r in res:
    print(r)

t2 = time.time()
print(t2-t1)