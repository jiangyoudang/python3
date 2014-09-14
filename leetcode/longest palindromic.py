class Solution:
    # @return a string
    def longestPalindrome(self, s):
        # dp

        # len_s = len(s)
        # m = [[0]*len_s for i in s]
        # max_m = 0
        # for i in range(0,len_s):
        #     for j in range(0,len_s):
        #         if s[j]==s[len_s-1-i]:
        #             m[i][j] = 1
        #             if i>1 and j>1:
        #                 m[i][j] += m[i-1][j-1]
        #                 if m[i][j]>max_m:
        #                     max_m = m[i][j]
        #
        # return max_m


        T = self.addSharp(s)
        len_T = len(T)
        p = [0]*len_T
        c, r = 0, 0
        for i in range(1,len(T)):
            i_mirror = c-(i-c)
            if r>i:
                p[i] = min(r-i,p[i_mirror])
            while i+1+p[i]<len_T and i-1-p[i]>=0 and T[i+1+p[i]]==T[i-1-p[i]]:
                p[i] += 1
            if r<i+p[i]:
                r = i+p[i]
                c = i
        max_p = max(p)
        max_i = p.index(max_p)
        i_start = (max_i-max_p)//2
        return s[i_start:i_start+max_p]

    def addSharp(self, s):
        s_ = '#'.join(s)
        s_ = '#'+s_+'#'
        return s_


test = Solution()
m = test.longestPalindrome('a')
# for line in m:
#     print(line)
print(m)