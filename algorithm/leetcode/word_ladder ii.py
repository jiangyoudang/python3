__author__ = 'congliu'


class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):

        if start not in dict:
            dict.append(start)
            #li.append(start)
        if end not in dict:
            dict.append(end)
        graph = self.build_graph(dict)
        queue = [start]
        graph[start]['visited'] = True
        while queue:
            curr = queue.pop(0)
            for nbr in graph[curr]['To']:
                if graph[nbr]['visited'] and graph[curr]['dis']+1>graph[nbr]['dis']:
                    continue
                if not graph[nbr]['visited']:
                    queue.append(nbr)
                    graph[nbr]['dis'] = graph[curr]['dis'] + 1
                    graph[nbr]['visited'] = True
                graph[nbr]['pre'].append(curr)

        return self.output(start,end,graph)

    def output(self,start,end, graph):
        if not graph[end]['pre']:
            if end == start:
                return [[start]]
            else:
                return []
        res = []
        for pre_v in graph[end]['pre']:
            for temp in self.output(start,pre_v,graph):
                temp.append(end)
                res.append(temp)
        return res

    def build_graph(self, dict):
        d = {}
        graph = {}

        for word in dict:
            graph[word] = {'To':[],'dis':0,'pre':[],'visited':False}
            for i in range(len(word)):
                bucket = word[:i] + '_' + word[i+1:]
                d[bucket] = d.get(bucket,[])
                d[bucket].append(word)
        for bucket in d.keys():
            for word1 in d[bucket]:
                for word2 in d[bucket]:
                    if word1 != word2:
                        graph[word1]['To'].append(word2)
        return graph


test = Solution()
#print(test.findLadders('a','b',['a','b','c']))
#print(test.findLadders('hot','dog',['hot','dog']))
#print(test.findLadders("hot", "dog", ["hot","cog","dog","tot","hog","hop","pot","dot"]))
