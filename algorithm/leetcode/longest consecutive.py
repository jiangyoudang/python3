class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        d = dict()
        max_n = 0
        for i in num:
            d[i] = 1
        for i in num:
            if not i in d:
                continue
            j=i+1
            while j in d:
                d[i] += d[j]
                del d[j]
                j += 1
            max_n = max(d[i], max_n)
        return max_n

res = Solution().longestConsecutive([0,-1])
print(res)
