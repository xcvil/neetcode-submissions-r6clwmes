class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: set() for i in range(n)}

        for k, v in edges:
            graph[k].add(v)
            graph[v].add(k)

        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in graph[node]:
                dfs(nei)
        
        connected = 0

        for i in range(n):
            if i not in visited:
                dfs(i)
                connected += 1
        return connected
        