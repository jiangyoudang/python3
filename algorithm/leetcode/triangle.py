class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        res = []
        for row in triangle:
            temp = res[:]
            res.append(0)
            for i in range(len(row)):
                if not temp:
                    res[0] = row[0]
                    break
                if i==0:
                    res[i] = temp[i] + row[i]
                elif i==len(row)-1:
                    res[i] = temp[-1] + row[i]
                else:
                    res[i] = min(temp[i-1], temp[i]) + row[i]

        print(res)
        return min(res)

test = Solution()
res = test.minimumTotal([[-1],[3,2],[1,-2,-1]])
print(res)
