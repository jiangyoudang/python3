class Node():
  def __init__(self, num):
    self.num = num
    self.neighbors = set()

  def connect(self, *args):
    for n in args:
      self.neighbors.add(n)

def main():
  nodes = [Node(i) for i in range(5)]
  nodes.append(Node(1))
  nodes[0].connect(nodes[1], nodes[2], nodes[5])
  nodes[1].connect(nodes[3], nodes[0])
  nodes[2].connect(nodes[0], nodes[3], nodes[4])
  nodes[3].connect(nodes[1], nodes[2], nodes[4])
  nodes[4].connect(nodes[2], nodes[3])
  nodes[5].connect(nodes[0])
  print(longest(nodes))


def longest(nodes):
  dp = {}
  for node in nodes:
    dfs(node, dp)
  ans = 0
  for k in dp:
    ans = max(ans, dp[k])
  print({k.num: dp[k] for k in dp})
  return ans

def dfs(curr, dp):
  if curr in dp:
    return dp[curr]
  dp[curr] = 1
  for next_node in curr.neighbors:
    if next_node.num == curr.num + 1:
      dp[curr] = max(dp[curr], dfs(next_node, dp) + 1)
  return dp[curr]



main()