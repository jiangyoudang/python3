class Solution(object):
  def maximalSquare(self, matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    if not matrix:
      return 0
    m = len(matrix)
    n = len(matrix[0])
    dp = [[0]*n for i in range(m)]
    maxSquare = 0

    for i in range(m):
      for j in range(n):
        if matrix[i][j] == '1':
          if i<1 or j<1:
            dp[i][j] = 1
          else:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+1
          if maxSquare < dp[i][j]:
            maxSquare = dp[i][j]

    return maxSquare*maxSquare

