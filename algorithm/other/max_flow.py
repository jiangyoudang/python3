from collections import deque, defaultdict
inf = float('inf')

def build_graph():
    graph = defaultdict(dict)

    graph['s'] = {'a': 1, 'c':2}
    graph['a'] = {'b': 1, 's':0, 'c':0}
    graph['b'] = {'t': 2, 'a':0, 'c':0}
    graph['c'] = {'b': 2, 'd':1, 's':0, 'a': 1}
    graph['d'] = {'t': 1, 'c':0}
    graph['t'] = {'b':0, 'd':0}

    return graph


# input:
#   s = 's', t = 't'; 2 end points
#

def bfs(graph, s, t):

    parent = {s:None}
    min_f = {s: inf}

    queue = deque()
    queue.append(s)
    while queue:
        if queue[-1] == t:
            break
        cur = queue.popleft()
        for node in graph[cur]:
            if node not in parent and graph[cur][node] > 0:
                min_f[node] = min(min_f[cur], graph[cur][node])
                parent[node] = cur
                queue.append(node)

    if not queue:
        return 0

    #build residual network
    flow = min_f[t]
    cur = t
    while parent[cur]:
        p = parent[cur]
        print(cur, end='')
        graph[p][cur] -= flow
        graph[cur][p] += flow
        cur = p
    print('{}  {}'.format(cur ,flow))
    return flow

def max_flow(graph):
    s = 's'
    t = 't'
    res = 0
    flow = bfs(graph, s, t)
    while flow > 0:
        res += flow
        flow = bfs(graph, s, t)

    return res

g = build_graph()
print(max_flow(g))
# print(g)
