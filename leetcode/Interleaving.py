class Solution:
    # @return a boolean

    '''#recursive  correct but TLE error
    def isInterleave(self, s1, s2, s3):
        if len(s3)==1:
            if s3==s2 or s1==s3: return True
            else: return False
        if not s2:
            return s1==s3
        if not s1:
            return s1==s2
        if not s3:
            return False

        if s3[0] == s2[0] and s1[0]==s3[0]:
            return self.isInterleave(s1,s2[1:],s3[1:]) or self.isInterleave(s1[1:],s2,s3[1:])
        elif s3[0]==s2[0]:
            return self.isInterleave(s1,s2[1:],s3[1:])
        elif s1[0]==s3[0]:
            return self.isInterleave(s1[1:],s2,s3[1:])
        else: return False
    '''
    #DP solution
    def isInterleave(self, s1, s2, s3):
        m = len(s1)
        n = len(s2)
        if len(s3)!= m+n:
            return False
        dp = [[False]*(n+1) for i in range(m+1)]
        dp[0][0]= True

        for i in range(1,m+1):
            dp[i][0] = (s3[i-1]==s1[i-1] and dp[i-1][0])
        for j in range(1,n+1):
            dp[0][j] = (s3[j-1]==s2[j-1] and dp[0][j-1])

        for i in range(1,m+1):
            for j in range(1,n+1):
                dp[i][j] = (s1[i-1]==s3[i+j-1] and dp[i-1][j]) or \
                            (s2[j-1]==s3[i+j-1] and dp[i][j-1])

        return dp[m][n]

# case_s1 = 'aabcc'
# case_s2 = 'dbbca'
case_s1 = 'abbbbbbcabbacaacccababaabcccabcacbcaabbbacccaaaaaababbbacbb'
case_s2 = "ccaacabbacaccacababbbbabbcacccacccccaabaababacbbacabbbbabc"
# case_s3 = 'aadbbcbcac'
# case_s3 = "aadbbbaccc"
case_s3 = "cacbabbacbbbabcbaacbbaccacaacaacccabababbbababcccbabcabbaccabcccacccaabbcbcaccccaaaaabaaaaababbbbacbbabacbbacabbbbabc"
res = Solution().isInterleave(case_s1,case_s2,case_s3)
print(res)