class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows==1:
            return s
        l = [list() for i in range(nRows)]
        i = 0
        direction = -1
        for c in s:
            if i%(nRows-1)==0:
                direction *= -1
            l[i].append(c)
            i += direction

        return ''.join([''.join(l[i]) for i in range(len(l))])


test = Solution()
res = test.convert("PAYPALISHIRING", 3)
print(res)
