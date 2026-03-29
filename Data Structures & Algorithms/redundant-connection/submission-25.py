class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {i:set() for i in range(1, len(edges)+1)}


        def dfs(curr, pare):
            if curr in visited:
                return True
            visited.add(curr)
            for nei in graph[curr]:
                if nei == pare:
                    continue
                if dfs(nei, curr):
                    return True
            return False

        for k, v in edges:
            visited = set()
            graph[k].add(v)
            graph[v].add(k)
            if dfs(k, v):
                return [k, v]
                

        