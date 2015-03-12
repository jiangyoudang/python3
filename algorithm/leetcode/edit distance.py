class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        m = len(word1)
        n = len(word2)

        c = [[0] * (m+1) for i in range(n+1)]

        for i in range(m+1):
            c[0][i] = i
        for j in range(n+1):
            c[j][0] = j

        for i in range(1, n+1):
            for j in range(1, m+1):
                if word1[j-1] == word2[i-1]:
                    c[i][j] = min(c[i-1][j-1], c[i][j-1]+1, c[i-1][j]+1)
                else:
                    c[i][j] = min(c[i-1][j-1]+1, c[i][j-1]+1, c[i-1][j]+1)

        return c[n][m]
