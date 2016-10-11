# binary index tree.


def getSum(BIT, index):
  _sum = 0
  while index > 0 :
    _sum += BIT[index]
    index -= index & -index

  return _sum

def update(BIT, index, val):
  _max = len(BIT)
  _diff = val - BIT[index]
  while index <= _max:
    BIT[index] += _diff
    index += index & -index



# 2D BIT
class NumMatrix(object):
  def __init__(self, matrix):
    """
    initialize your data structure here.
    :type matrix: List[List[int]]
    """
    if not matrix:
      return
    self.m = len(matrix)
    self.n = len(matrix[0])
    self.matrix = [[0]*self.n for _ in range(self.m)]
    self.BIT = [[0] * (self.n + 1) for _ in range(self.m + 1)]
    for i in range(self.m):
      for j in range(self.n):
        self.update(i, j, matrix[i][j])

  def update(self, row, col, val):
    """
    update the element at matrix[row,col] to val.
    :type row: int
    :type col: int
    :type val: int
    :rtype: void
    """
    x, y = row + 1, col + 1
    diff = val - self.matrix[row][col]
    self.matrix[row][col] = val
    while x <= self.m:
      y1 = y
      while y1 <= self.n:
        self.BIT[x][y1] += diff
        y1 += y1 & -y1
      x += x & -x

  def sum(self, row, col):
    if row<0 or col < 0:
      return 0
    x, y = row + 1, col + 1
    result = 0
    while x > 0:
      y1 = y
      while y1 > 0:
        result += self.BIT[x][y1]
        y1 -= y1 & -y1
      x -= x & -x
    return result

  def sumRegion(self, row1, col1, row2, col2):
    """
    sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
    :type row1: int
    :type col1: int
    :type row2: int
    :type col2: int
    :rtype: int
    """
    return self.sum(row2, col2) - self.sum(row2, col1-1) - self.sum(row1-1, col2) + self.sum(row1-1, col1-1)

matrix =  [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

# Your NumMatrix object will be instantiated and called as such:
numMatrix = NumMatrix(matrix)
print(numMatrix.sumRegion(0, 1, 2, 3))
numMatrix.update(1, 1, 10)
print(numMatrix.sumRegion(1, 2, 3, 4))
