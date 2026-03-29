class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = {i: set() for i in range(n)}

        for k, v in edges:
            graph[k].add(v)
            graph[v].add(k)

        visited = set()

        def dfs(i):
            if i in visited:
                return
            visited.add(i)
            for nei in graph[i]:
                dfs(nei)
        c = 0

        for i in graph:
            if i not in visited:
                dfs(i)
                c += 1

        return c
        