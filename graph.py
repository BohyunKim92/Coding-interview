print('Depth First Search')
def explore(g: dict[str, list[str]], visited: set, path: list[str], v: str) -> list[str]:
    visited.add(v)
    path.append(v)
    for n in g[v]:
        if n not in visited:
            explore(g,visited,path,n)
    return path

def dfs(g: dict[str,list[str]], s: str)-> list[str]:
    visited = set()
    path = []
    return explore(g,visited,path,s)

g1 = {
    'A': ['B'],
    'B': ['A'],
    'C': ['D'],
    'D': ['C'],
    'E': []
}
print(dfs(g1,'A'))