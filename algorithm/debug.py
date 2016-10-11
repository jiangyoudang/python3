class Solution:
  # @param {int[][]} A an integer matrix
  # @return {int}  an integer
  def longestIncreasingContinuousSubsequenceII(self, A):
    # Write your code here
    self.dp = {}
    rows = len(A)
    cols = len(A[0])
    for i in range(rows):
      for j in range(cols):
        if (i, j) not in self.dp:
          self.dfs(A, (i, j), set())
    return max(self.dp.values())

  def dfs(self, matrix, point, visited):
    if point in self.dp:
      return self.dp[point]
    x, y = point
    v = matrix[x][y]
    visited.add(point)
    direction = ((-1, 0), (0, 1), (0, -1), (1, 0))
    for dx, dy in direction:
      if (0 <= x + dx < len(matrix) and 0 <= y + dy < len(matrix[0])
          and matrix[x + dx][y + dy] > v and (x+dx, y+dy) not in visited):
        self.dp[point] = max(self.dp.get(point, 1),
                             self.dfs(matrix, (x + dx, y + dy), visited) + 1)
    visited.remove(point)
    self.dp[point] = self.dp.get(point, 1)
    return self.dp[point]


A = [[1,5,3],[4,10,9],[2,8,7]]
res = Solution().longestIncreasingContinuousSubsequenceII(A)
print(res)