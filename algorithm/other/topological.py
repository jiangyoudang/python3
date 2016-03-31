from collections import defaultdict, deque

def topo_traversal(graph, visited, start_v, res):
  # DFS with stack
  visited[start_v] = True

  for v in graph[start_v]:
    if not visited[v]:
      topo_traversal(graph, visited, v, res)

  res.append(start_v)

def topo_bfs(graph):
  res = []
  cycle = False
  # indegree = defaultdict(lambda :0)
  indegree = {i: 0 for i in range(6)}
  for node in graph:
    for edge in graph[node]:
      indegree[edge] += 1
  print(indegree)
  queue = deque()
  for node, degree in indegree.items():
    if degree == 0:
      queue.append(node)
  while queue:
    curr = queue.popleft()
    res.append(curr)
    for next_node in graph[curr]:
      indegree[next_node] -= 1
      if indegree[next_node] == 0:
        queue.append(next_node)

  for node, degree in indegree.items():
    if degree:
      cycle = True
  return res, cycle


def build_graph():
  graph = defaultdict(list)

  graph[5] = [2, 0]
  graph[2] = [3]
  graph[3] = [1]
  graph[4] = [0, 1]

  return graph


g = build_graph()
visited = [False] * 6
res = []

for i in [0, 1, 2, 3, 4, 5]:
  if not visited[i]:
    topo_traversal(g, visited, i, res)

print(res[::-1])
result, cycle = topo_bfs(g)
print(cycle)
print(result)

class Solution(object):
  def alienOrder(self, words):
    """
    :type words: List[str]
    :rtype: str
    """
    # build grap
    graph = {c: set() for c in set(''.join(words))}
    for i in range(1, len(words)):
      word0 = words[i - 1]
      word1 = words[i]
      for j in range(min(len(word0), len(word1))):
        if word0[j] != word1[j]:
          char0, char1 = word0[j], word1[j]
          graph[char1].add(char0)
          break
    # topological sort
    self.cycle = False
    result = []
    visited = set()
    for c in graph:
      if c not in visited:
        self.topo_sort(graph, c, visited, result, [c])
    if self.cycle:
      return ''
    return ''.join(result)

  def topo_sort(self, graph, start, visited, result, tmp):

    visited.add(start)
    for next_c in graph.get(start, []):
      if next_c in tmp:
        self.cycle = True
        return
      if next_c not in visited:
        tmp.append(next_c)
        self.topo_sort(graph, next_c, visited, result, tmp)
        tmp.pop()

    result.append(start)
