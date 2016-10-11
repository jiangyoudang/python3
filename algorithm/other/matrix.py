
matrix = ['00100', '00000', '01001', '10000', '00000']

def countPaths(matrix):
  rows = len(matrix)
  cols = len(matrix)
  steps = [[0] * cols for i in range(rows)]

  # initiate
  for row in range(1, rows):
    if matrix[row][0] == '1':
      break
    steps[row][0] = 1

  for col in range(1, cols):
    if matrix[0][col] == '1':
      break
    steps[0][col] = 1

  for row in range(1, rows):
    for col in range(1, cols):
      if matrix[row][col] == '1':
        steps[row][col] = 0
      else:
        steps[row][col] = steps[row-1][col] + steps[row][col-1]

  print(steps)
  return steps[rows-1][cols-1]



print(countPaths(matrix))




def countPaths2(rows_num, cols_num, stop_steps):
  start = (rows_num-1, 0)
  directions = (
    (-1, 0), (0, 1), (1, 0), (0, -1)
  )
  steps = [[0] * cols_num for i in range(rows_num)]
  steps[rows_num-1][0] = 1
  points = [start]
  step_num = 0

  while points:
    next_points = []
    for point in points:
      for dx, dy in directions:
        new_x, new_y = point[0] + dx, point[1] + dy
        if 0 <= new_x < rows_num and 0 <= new_y < cols_num:
          steps[new_x][new_y] += steps[point[0]][point[1]]
          next_points.append((new_x, new_y))

    for point in points:
      steps[point[0]][point[1]] = 0
    step_num += 1
    points = next_points
    if step_num == stop_steps:
      return steps

print(countPaths2(5, 5, 3))





