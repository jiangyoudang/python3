
from collections import deque

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None
        queue = deque()
        queue.append(node)
        node_copy = UndirectedGraphNode(node.label)
        map_d = {node:node_copy}
        while queue:
            curr = queue.popleft()
            for node_t in curr.neighbors:

                #NOTE: " node_t in map_d.keys()" in python2 takes O(n) times, not O(1)
                if not node_t in map_d:
                    queue.append(node_t)
                    map_d[node_t] = UndirectedGraphNode(node_t.label)
                map_d[curr].neighbors.append(map_d[node_t])

        return map_d[node]

    #word search
    def exist(self, board, word):
        start = []
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    start.append((i,j))


        for i,j in start:
            cache = set()
            if self.search(board, word, m, n, i,j,cache):
                return True

        return False


    def search(self, board, word, m, n, i, j, cache):
        cache_tmp = cache.copy()
        if not word:
            return True
        if i>=m or i<0 or j>=n or j<0 or (i,j) in cache_tmp or board[i][j] != word[0]:
            return False
        cache_tmp.add((i,j))
        return  self.search(board, word[1:], m,n, i+1, j, cache_tmp) or \
                self.search(board, word[1:], m,n, i-1, j, cache_tmp) or \
                self.search(board, word[1:], m,n, i, j+1, cache_tmp) or \
                self.search(board, word[1:], m,n, i, j-1, cache_tmp)

test_board = ["ABCE","SFES","ADEE"]
test_word = "ABCESEEEFS"
res = Solution().exist(test_board, test_word)
# res = Solution().search(test_board, test_word, 3,4,0,0,set())
print(res)
