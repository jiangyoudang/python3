class Solution(object):
  def numIslands2(self, m, n, positions):
    """
    :type m: int
    :type n: int
    :type positions: List[List[int]]
    :rtype: List[int]
    """

    self.parent = {}
    self.rank = {}
    self.islands = 0
    self.result = []

    directions = ((-1,0), (0, 1), (1, 0), (0, -1))
    positions = list(map(lambda x:tuple(x), positions))

    for pos in positions:
      print(self.parent)
      if pos not in self.parent:
        self.make_point(pos)
        for dx, dy in directions:
          x, y = pos
          next_x, next_y = x+dx, y+dy
          if (0 <= next_x < m and 0 <= next_y < n
              and (next_x, next_y) in self.parent):
            self.union(pos, (next_x, next_y))
        self.result.append(self.islands)
    return self.result

  def make_point(self, point):
    self.parent[point] = point
    self.rank[point] = 0
    self.islands += 1

  def find(self, point):
    if self.parent[point] != point:
      self.parent[point] = self.find(self.parent[point])
    return self.parent[point]

  def union(self, x, y):
    parent_x = self.find(x)
    parent_y = self.find(y)
    if parent_x != parent_y:
      if self.rank[parent_x] < self.rank[parent_y]:
        self.parent[parent_x] = parent_y
      elif self.rank[parent_x] > self.rank[parent_y]:
        self.parent[parent_y] = parent_x
      else:
        self.parent[parent_y] = parent_x
        self.rank[parent_x] += 1
      self.islands -= 1



m = 3
n = 3
pos = [[0,0],[0,1],[1,2],[2,1]]
print(Solution().numIslands2(m, n, pos))
