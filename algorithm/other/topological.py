from collections import defaultdict

def topo_traversal(graph, visited, start_v, res):

    # DFS with stack
    visited[start_v] = True

    for v in graph[start_v]:
        if not visited[v]:
            topo_traversal(graph, visited, v, res)


    res.append(start_v)



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


for i in [0, 1,2,3,4,5]:
    if not visited[i]:
        topo_traversal(g, visited, i, res)


print(res[::-1])