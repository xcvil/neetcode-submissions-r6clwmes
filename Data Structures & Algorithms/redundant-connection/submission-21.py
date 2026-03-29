class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {i:set() for i in range(1, len(edges)+1)}

        for k, v in edges:
            graph[k].add(v)
            graph[v].add(k)

        visited = set()
        cycle = set()
        isCycleStart = -1

        def dfs(curr, pare):
            nonlocal isCycleStart
            if curr in visited:
                isCycleStart = curr
                return True
            visited.add(curr)

            for nei in graph[curr]:
                if nei == pare:
                    continue
                if dfs(nei, curr):
                    if isCycleStart != -1:
                        cycle.add(curr)
                    if isCycleStart == curr: # here curr
                        isCycleStart = -1
                    return True
            return False

        dfs(1, -1)
        for k, v in reversed(edges):
            if k in cycle and v in cycle:
                return [k, v]

        return []
