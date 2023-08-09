class Solution:
    def canFinish(self, num: int, A: list[list[int]]) -> bool:
        graph = [[] for _ in range(num)]
        for k, v in A:
            graph[v].append(k)
        visited = [-1] * num
        for i in range(num):
            if visited[i] == -1:
                if not self.func(i, graph, visited):
                    return False

        return True

    
    def func(self, node: int, graph: list, visited: list) -> bool:
        visited[node] = 0
        result = 1
        for i in graph[node]:
            if visited[i] == -1:
                result &= self.func(i,graph,visited)
            else:
                result &= visited[i]
        if result == 1:
            visited[node] = 1
            return True
        return False
        