
def find(board, word, pos, visited):
    directions = [(1,0), (0,1), (-1,0), (0,-1)]

    found = False
    if not word:
        return True
    for direction in directions:
        x, y = pos
        x_di, y_di = direction
        x += x_di
        y += y_di
        if 0 <= x < len(board) and 0 <= y < len(board[0]):
            if (x, y) not in visited and board[x][y] == word[0]:
                visited.add((x,y))
                found = find(board, word[1:], (x,y), visited) or found
                if found:
                    return True
                visited.remove((x,y))

    return found

def exist(board, word):
    m = len(board)
    n = len(board[0])
    if not board or n==0:
        return False
    if not word:
        return False
    for i in range(m):
        for j in range(n):
            if board[i][j] == word[0]:
                if find(board, word[1:], (i,j), {(i,j)}):
                    return True
    return False




class Solution(object):
  def findWords(self, board, words):
    """
    :type board: List[List[str]]
    :type words: List[str]
    :rtype: List[str]
    """
    trie = self.makeTrie(words)
    self.trie = trie
    m = len(board)
    n = len(board[0])
    result = []
    for i in range(m):
      for j in range(n):
        if board[i][j] in trie:
          self.searchWord(board, trie[board[i][j]], (i, j), [(i,j)], result)
    print(trie)
    return result

  def clean(self, board, trie, path, i):
    if i == len(path):
      del trie['$']
      return
    pos = path[i]
    char = board[pos[0]][pos[1]]
    self.clean(board, trie[char], path, i+1)
    if not trie[char]:
      del trie[char]

  def searchWord(self, board, trie, pos, path, result):
    if '$' in trie:
      result.append(''.join([board[point[0]][point[1]] for point in path]))
      # clean trie to remove the found word making following search faster
      self.clean(board, self.trie, path, 0)

    m = len(board)
    n = len(board[0])
    directions = ((-1, 0), (1,0), (0,1), (0,-1))

    x, y = pos
    for dx, dy in directions:
      x1, y1 = x+dx, y+dy
      if (0<=x1<m and 0<=y1<n
          and (x1, y1) not in path
          and board[x1][y1] in trie):
        path.append((x1, y1))
        self.searchWord(board, trie[board[x1][y1]], (x1, y1), path, result)
        path.pop()


  def makeTrie(self, words):
    # end word with '$'
    trie = {}
    for word in words:
      root = trie
      for char in word:
        root[char] = root.get(char, {})
        root = root[char]
      root['$'] = '$'
    return trie


# words = ["oath", "pea", "eat", "rain"]
# board = [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]

board = ["oaan","etae","ihkr","iflv"]
words = ["oath","pea","eat","rain"]

board1 = ["ab","aa"]
words1 = ["aba","baa","bab","aaab","aaa","aaaa","aaba"]
# board2 = ['va','bd', 'en']
# words2 = ['bend', 'benda', 'abc']
print(Solution().findWords(board, words))
print(Solution().findWords(board1, words1))
