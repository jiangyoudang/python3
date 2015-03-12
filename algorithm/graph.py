
def build_graph(vertices_num, edges):
    graph = [['N']*vertices_num for i in range(vertices_num)]

    for edge in edges:
        graph[edge[0]][edge[1]] = True
    return graph

print(build_graph(5, []))