from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses == 1 or not prerequisites:
            return True

        graph = self.construct_graph(numCourses, prerequisites)
        print(graph)
        for node in range(numCourses):
            # go over each course
            visited = set()
            if self.exist_cycle(node, visited, graph):
                return False
        
        return True

    def exist_cycle(self, node: int, visited: set[int],
    graph: dict[int, set[int]])->bool:
        """determine if there is a cycle or not given the starting node."""
        print(node)
        if node in visited:
            # there is a cycle
            return True

        visited.add(node)
        if node not in graph or not graph[node]:
            # already explored or the end of the graph
            return False
        
        while graph[node]:
            child = graph[node].pop()
            if self.exist_cycle(child, visited, graph):
                return True
            visited.remove(child)
        return False

    
    def construct_graph(self, num_courses: int, 
    prerequisites: List[List[int]]) -> dict[int, set[int]]:
        """construct graph based on prerequisites"""
        graph = dict()
        course_order = set()
        
        for course, pre_course in prerequisites:
            if pre_course not in graph:
                graph[pre_course] = set()
            graph[pre_course].add(course)
        
        return graph
            
