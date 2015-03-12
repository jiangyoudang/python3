class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        m = len(S)
        n = len(T)
        dp = [[0] * (m+1) for i in range(n+1)]
        for j in range(m+1):
            dp[0][j] = 1

        for i in range(1,n+1):
            for j in range(1,m+1):
                if T[i-1] == S[j-1]:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-1]

        # return dp[n][m]
        return dp

# test_case = ['rabbbit','rabbit']
test_case = ['rerfsafwfr','r']
res = Solution().numDistinct(*test_case)
for i in range(len(res)):
    print(res[i])