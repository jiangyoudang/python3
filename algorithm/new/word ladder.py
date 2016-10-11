import collections

class Solution(object):
  def findLadders(self, beginWord, endWord, wordlist):
    """
    :type beginWord: str
    :type endWord: str
    :type wordlist: Set[str]
    :rtype: List[List[int]]
    """
    self.d = collections.defaultdict(set)
    self.length = len(beginWord)
    self.begin = beginWord
    self.end = endWord
    self.output = collections.defaultdict(set)

    all_words = set(wordlist)
    all_words.add(beginWord)
    all_words.add(endWord)
    self.makeMap(all_words)

    self.bfs()
    result = []
    self.printResult(endWord, [], result)
    return result


  def makeMap(self, words):
    for i in range(self.length):
      for word in words:
        key = word[:i] + '*' + word[i+1:]
        self.d[key].add(word)

  def getEdge(self, word):
    edges = set()
    if word == self.end:
      return edges
    for i in range(self.length):
      key = word[:i] + '*' + word[i+1:]
      edges |= self.d[key]
      edges.remove(word)
    return edges

  def bfs(self):
    curr = [self.begin]
    visited = set()
    while curr:
      next_curr = []
      for word in curr:
        edges = self.getEdge(word)
        for edge in edges:
          if edge not in visited:
            if edge not in next_curr:
              next_curr.append(edge)
            if edge not in curr:
              self.output[edge].add(word)
        visited.add(word)
      curr = next_curr

  def printResult(self, endword, tmp, result):
    if endword == self.begin:
      result.append([self.begin] + tmp[::-1])
      return

    for word in self.output[endword]:
      tmp.append(endword)
      self.printResult(word, tmp, result)
      tmp.pop()


wordlist = ["hot","dot","dog","lot","log"]
begin = 'hit'
end = 'cog'
s = Solution()
print(s.findLadders(begin, end, wordlist))
