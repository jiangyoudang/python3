from collections import defaultdict

def find(graph, start, end, k):
  m = len(graph)
  n = len(graph[0])
  directions = (
    (-1,0), (0, 1), (1, 0), (0, -1)
  )
  level1 = {start: 1}
  for _ in range(k):
    level2 = defaultdict(lambda :0)
    for point in level1:
      for dx, dy in directions:
        x, y = dx + point[0], dy +point[1]
        new_point = (x, y)
        if 0 <= x < m and 0 <= y < n:
          level2[new_point] += level1[point]
    level1 = level2
    print(level1)
  return level1[end]

g = [
  [0,0,0],
  [0,0,0],
  [0,0,0],
]
print(find(g, (0,1), (1,2), 4))
