class Vector2D(object):
  def __init__(self, vec2d):
    """
    Initialize your data structure here.
    :type vec2d: List[List[int]]
    """
    self.data = vec2d
    self.next_pos = (0, -1)

  def next(self):
    """
    :rtype: int
    """
    x, y = self.next_pos
    return self.data[x][y]

  def hasNext(self):
    """
    :rtype: bool
    """
    if not self.data:
      return False
    x, y = self.next_pos
    if y < len(self.data[x])-1:
      self.next_pos = (x, y+1)
      return True
    x += 1
    while x < len(self.data):
      if not self.data[x]:
        x += 1
      else:
        self.next_pos = (x, 0)
        return True
    return False
    # Your Vector2D object will be instantiated and called as such:
    # i, v = Vector2D(vec2d), []
    # while i.hasNext(): v.append(i.next())
