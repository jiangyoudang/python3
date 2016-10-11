class Solution(object):
  def numberOfPatterns(self, m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    self.result = 0
    self.m = m
    self.n = n
    self.numbers = range(1, 10)
    for i in self.numbers:
      self.find(i, [i])
    return self.result

  def find(self, start, path):
    if self.m <= len(path) <= self.n:
      self.result += 1
    for next_n in self.getNext(start, path):
      path.append(next_n)
      self.find(next_n, path)
      path.pop()

  def getNext(self, start, path):
    corners = (1, 3, 7, 9)
    nexts = []
    if len(path) <= self.n:
      for i in self.numbers:
        if i not in path:
          # pass through 5
          if start + i == 10 and 5 not in path:
            continue
          # pass through corner
          elif start in corners and i in corners:
            if (start + i) // 2 not in path:
              continue
          nexts.append(i)
    return nexts


print(Solution().numberOfPatterns(1,3))
