class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()

        graph = {i: set() for i in range(n)}

        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        def dfs(curr, pare):
            if curr in visited:
                return False
            
            visited.add(curr)
            for nei in graph[curr]:
                if nei == pare:            # ← 加这个
                    continue
                if not dfs(nei, curr):
                    return False
            return True

        if not dfs(0, -1):
            return False

        return len(visited) == n