class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean

    #'solution 1
    #dp, time cost N^2

    # def isMatch(self, s, p):
    #     s_len = len(s)
    #     p_len = len(p)
    #     dp = [[False for i in range(s_len+1)] for j in range(p_len+1)]
    #     dp[0][0] = True
    #
    #     for j in range(1,p_len+1):
    #         for i in range(1,s_len+1):
    #             if dp[j-1][i-1] and (s[i-1] == p[j-1] or p[j-1]=='?'):
    #                 dp[j][i] = True
    #                 break
    #             elif p[j-1] == '*':
    #                 if dp[j-1][i-1]:
    #                     dp[j-1][i-1:] = [True for k in dp[j-1][i-1:]]
    #                     break
    #
    #     return dp[j][i]


    def isMatch(self, s, p):
        len_s = len(s)
        len_p = len(p)
        p_pointer = 0
        s_pointer = 0
        ss = 0
        star = -1

        while s_pointer < len_s:
            if p_pointer<len_p and (p[p_pointer]==s[s_pointer] or p[p_pointer]=='?'):
                p_pointer += 1
                s_pointer += 1
            elif p_pointer<len_p and p[p_pointer]=='*':
                star = p_pointer
                ss = s_pointer
                p_pointer += 1
            elif star!=-1:
                ss += 1
                s_pointer = ss
                p_pointer = star+1
            else:
                return False

        while p_pointer<len_p and p[p_pointer]=='*':
            p_pointer += 1
        return p_pointer==len_p

test = Solution()
if test.isMatch('a','aaaa'):
    print('True')
else:
    print('False')