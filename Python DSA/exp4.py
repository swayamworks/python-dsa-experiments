def DLS(graph, node, goal, limit):
    if node==goal:
        return [node]
    if limit==0:
        return None
    for child in graph[node]:
        result= DLS(graph, child, goal, limit-1)
        if result is not None:
            return [node] + result 
    return None
def DFID(graph, start, goal, mdepth):
    for depth in range(mdepth + 1):
        print("trying depth", depth)
        result = DLS(graph, start, goal, depth)
        if result is not None:
            return result 
    return None
graph = {
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

start = 'A'
goal = 'G'

path = DFID(graph, start, goal, 10)
print("\nSolution Path:", path)