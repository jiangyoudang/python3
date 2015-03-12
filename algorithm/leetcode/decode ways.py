class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        l = len(s)
        num_pre2 = 1
        num_pre1 = 1
        if s:
            pre = s[0]
            if pre == '0':
                num_pre1 = 0
        else:
            return 0


        if l>1:
            for i in s[1:]:
                if pre == '0':
                    if pre+i == '00':
                        return 0
                    num_pre2 = num_pre1
                elif i == '0':
                    if int(pre+i)>26:
                        return 0
                    num_pre1 = num_pre2
                elif int(pre+i) <= 26:
                    num_pre1, num_pre2 = num_pre2 + num_pre1, num_pre1
                else:
                    num_pre2 = num_pre1

                pre = i
            return num_pre1

        return num_pre1


test = Solution()

# '1212', '100', '001', '101', '230'
res = test.numDecodings('230')
print(res)