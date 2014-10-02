import time

class Solution:
    # @return a boolean

    # recursive
    def isMatch(self, s, p):
        if not p:
            return len(s) == 0
        if len(p) == 1 or p[1]!='*':
            if not s or (s[0]!=p[0] and p[0]!='.'):
                return False
            return self.isMatch(s[1:],p[1:])
        else:
            i = -1; len_s = len(s)
            while i<len_s and (i<0 or p[0]==s[i] or p[0]=='.'):
                if self.isMatch(s[i+1:],p[2:]):
                    return True
                i += 1
            return False

    # DP
    def isMatch1(self, s, p):
        s_len = len(s)
        p_len = len(p)
        dp = [[False for i in range(p_len+1)] for j in range(s_len+1)]
        dp[0][0] = True

        for i in range(1,p_len):
            if p[i]=='*':
                dp[0][i+1] = dp[0][i-1]

        for i in range(1,s_len+1):
            for j in range(1,p_len+1):
                if p[j-1]=='.' or p[j-1]==s[i-1]:
                   dp[i][j] =dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-2] or dp[i][j-1] or (dp[i-1][j] and (s[i-1]==p[j-2] or p[j-2]=='.'))

        return dp[s_len][p_len]

# res = Solution().isMatch1('a','ab*a')
# res = Solution().isMatch1('','.*')
# res = Solution().isMatch1('aa','a*')
test_str = ["aaaaaaaaaaaaaabc", "a*a*a*a*a*a*a*a*a*a*b"]
t0 = time.time()
res = Solution().isMatch(*test_str)
t1 = time.time()
res2 = Solution().isMatch1(*test_str)
t2 = time.time()
print(t1-t0)
print(t2-t1)

print(res)