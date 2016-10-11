class Solution(object):
  def shortestDistance(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    m = len(grid)
    n = len(grid[0])
    shortest = float('inf')
    buildings = sum([1 for row in grid for land_val in row if land_val == 1])

    for i in range(m):
      for j in range(n):
        if grid[i][j] == 0:
          dist = self.bfs(grid, (i,j), buildings)
          if dist != -1 and shortest > dist:
            shortest = dist
    return shortest

  def bfs(self, grid, start, total_buildings):
    m = len(grid)
    n = len(grid[0])
    curr_step = [start]
    directions = (
      (-1, 0), (1,0), (0,1), (0,-1)
    )
    total_distance = 0
    distances = {start:0}
    buildings_visited = 0
    while curr_step:
      next_step = []
      for pos in curr_step:
        x,y = pos
        for dx, dy in directions:
          next_pos = (x+dx, y+dy)
          if 0<=next_pos[0]< m and 0<=next_pos[1]< n and next_pos not in distances:
            land_val = grid[next_pos[0]][next_pos[1]]
            distances[next_pos] = distances[pos] + 1
            if land_val == 0:
              next_step.append((next_pos))
            elif land_val == 1:
              total_distance += distances[next_pos]
              buildings_visited += 1
              if buildings_visited == total_buildings:
                return total_distance

      curr_step = next_step

    return -1



grid = [
  [1 , 0 , 2 , 0 , 1],
  [0 , 0 , 0 , 0 , 0],
  [0 , 0 , 1 , 0 , 0]
]

print(Solution().shortestDistance(grid))


