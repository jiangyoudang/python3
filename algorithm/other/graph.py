from random import random, randrange
from collections import deque


def build_graph(vertices_num, edges):
  graph = [['N'] * vertices_num for i in range(vertices_num)]

  for edge in edges:
    graph[edge[0]][edge[1]] = True
  return graph


# print(build_graph(5, []))


def build_m(m, n):
  matrix = [[0] * n for i in range(m)]
  for i in range(m):
    for j in range(n):
      if random() >= 0.5:
        matrix[i][j] = 1

  return matrix


def print_matrix(matrix):
  m = len(matrix)
  n = len(matrix[0])
  for i in range(m):
    print(''.join(map(str, matrix[i])))


def bfs(matrix, startpoint, visited):
  '''
  bfs search
  :param matrix:
  :param startpoint: tuple of point
  :param visited: set
  :return:
  '''
  m = len(matrix)
  n = len(matrix[0])
  directions = [
    (-1, 0), (0, 1), (1, 0), (0, -1)
  ]
  count = 0

  queue = deque()
  queue.append(startpoint)
  visited.add(startpoint)
  while queue:
    curr_x, curr_y = queue.popleft()
    print(curr_x*n+curr_y, end=' ')
    count += 1
    for dir_x, dir_y in directions:
      next_x, next_y = curr_x + dir_x, curr_y + dir_y
      if 0 <= next_x <= m - 1 and 0 <= next_y <= n - 1 and (next_x, next_y) not in visited:  # |set(queue):
        queue.append((next_x, next_y))
        visited.add((next_x, next_y))
  return count


def dfs(matrix, startpoint, visited, count):
  m = len(matrix)
  n = len(matrix[0])
  directions = [
    (-1, 0), (0, 1), (1, 0), (0, -1)
  ]
  # print(startpoint)
  curr_x, curr_y = startpoint
  print(curr_x * n + curr_y, end=' ')
  visited.add(startpoint)
  count[0] += 1
  for dir_x, dir_y in directions:
    next_x, next_y = curr_x + dir_x, curr_y + dir_y
    if 0 <= next_x <= m - 1 and 0 <= next_y <= n - 1 and (
    next_x, next_y) not in visited:  # |set(queue):
      # if matrix[next_x][next_y] == matrix[curr_x][curr_y]:
      dfs(matrix, (next_x, next_y), visited, count)


# m,n = 5, 10
# res = [0]
# startpoint = (randrange(m), randrange(n))
#
# matrx = build_m(m, n)
# print('start from', startpoint, matrx[startpoint[0]][startpoint[1]])
# print_matrix(matrx)
# print('bfs count',bfs(matrx, startpoint, set()))
# dfs(matrx, startpoint, set(), res)
# print('dfs count', res[0])

def dfs_stack(matrix, startpoint, visited):
  m = len(matrix)
  n = len(matrix[0])
  directions = [
    (-1, 0), (0, 1), (1, 0), (0, -1)
  ]
  stack = [startpoint]
  # print(startpoint)
  while stack:
    curr = stack[-1]
    curr_x, curr_y = curr
    if curr not in visited:
      num = curr_x * n + curr_y
      print(num, end=' ')
      visited.add(curr)
    for dir_x, dir_y in directions:
      next_x, next_y = curr_x + dir_x, curr_y + dir_y
      if 0 <= next_x <= m - 1 and 0 <= next_y <= n - 1 and (
      next_x, next_y) not in visited:  # |set(queue):
        # if matrix[next_x][next_y] == matrix[curr_x][curr_y]:
        stack.append((next_x, next_y))
        # visited.add((next_x, next_y))
        break
    else:
      stack.pop()


def dfs_stack2(matrix, startpoint, visited):
  m = len(matrix)
  n = len(matrix[0])
  directions = [
    (-1, 0), (0, 1), (1, 0), (0, -1)
  ]
  stack = [startpoint]
  visited.add(startpoint)
  while stack:
    curr_x, curr_y = stack.pop()
    print(curr_x * n + curr_y, end=' ')
    for dx, dy in directions:
      next_x = dx + curr_x
      next_y = dy + curr_y
      if 0<= next_x <m and 0<= next_y<n and (next_x, next_y) not in visited:
        stack.append((next_x, next_y))
        visited.add((next_x, next_y))


def dfs_iter(matrix, startpoint, visited):
  m = len(matrix)
  n = len(matrix[0])
  directions = [
    (-1, 0), (0, 1), (1, 0), (0, -1)
  ]
  stack = [startpoint]
  while stack:
    curr = stack.pop()
    visited.add(curr)
    x, y = curr
    print(x*n+y, end=' ')
    for dx, dy in directions:
      nx, ny = x+dx, y+dy
      npoint = (nx, ny)
      if 0<= nx < m and 0<= ny < n and npoint not in visited:
        stack.append(npoint)
        visited.add(npoint)

matrix_test = [[i * 5 + j for j in range(5)] for i in range(5)]
for i in range(5):
  print(matrix_test[i])
res = [0]
dfs(matrix_test, (3, 2), set(), res)
print('{:*^80}'.format('split'))
dfs_stack(matrix_test, (3, 2), set())
print('{:*^80}'.format('split'))
dfs_iter(matrix_test, (3, 2), set())
print('{:*^80}'.format('split'))
dfs_stack2(matrix_test, (3, 2), set())
print('{:*^80}'.format('split'))
bfs(matrix_test, (3,2), set())

