"""This is a docstring for depth first search. """

def explore_graphs(graph: dict[str, list[str]], visited: set,
                    path: list[str], vertex: str) -> list[str]:
    """
    Explore graph based on graph, visited node, path and v. 
    """
    visited.add(vertex)
    path.append(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            explore_graphs(graph, visited, path, neighbor)
    return path

def depth_first_search(graph: dict[str,list[str]], source: str)-> list[str]:
    """
    given a graph and source node, return
    """
    visited = set()
    path = []
    return explore_graphs(graph,visited,path,source)

def main():
    """Execute graph_example_1"""
    print('Depth First Search')
    graph_example_1 =  {
        "a" : ["b","c"],
        "b" : ["a", "d"],
        "c" : ["a", "d"],
        "d" : ["e"],
        "e" : ["d"]
        }
    print(depth_first_search(graph_example_1,"a"))


if __name__ == '__main__':
    main()
