import time

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def __init__(self):
        self.cache = {}

    # def wordBreak(self, s, dict):
    #     for i in range(len(s)):
    #         if s[:i+1] in dict:
    #             self.cache[i+1] = [[s[:i+1]]]
    #         keys = list(self.cache.keys())
    #         for k in keys:
    #             if s[k:i+1] in dict:
    #                 new = self.cache.get(i+1,[])
    #                 for temp in self.cache[k]:
    #                     #temp.append(s[k:i+1])
    #                     new.append(temp+[s[k:i+1]])
    #                 self.cache[i+1] = new
    #
    #     result = []
    #     if self.cache.get(len(s)):
    #         for solution in self.cache[len(s)]:
    #             result.append(' '.join(solution))
    #     return result

    def wordBreak(self, s, dict):
        for i in range(len(s),-1,-1):
            if s[i:] in dict:
                self.cache[i] = [[s[i:]]]
            keys = list(self.cache.keys())
            for k in keys:
                if s[i:k] in dict:
                    new = self.cache.get(i,[])
                    for temp in self.cache[k]:
                        #temp.append(s[k:i+1])
                        new.append([s[i:k]]+temp)
                    self.cache[i] = new

        result = []
        if self.cache.get(0):
            for solution in self.cache[0]:
                result.append(' '.join(solution))
        return result

time0 = time.time()

print(Solution().wordBreak("catsanddog",["cat", "cats", "and", "sand", "dog"]))
#print(Solution().wordBreak('''baaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab''',
                           # ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))

time1 = time.time()
print('Time cost: {}'.format(time1-time0))