class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {i:set() for i in range(1, len(edges)+1)}

        for k, v in edges:
            graph[k].add(v)
            graph[v].add(k)

        visited = set()
        cycle = set()
        cycleStart = -1

        def dfs(curr, pare):
            nonlocal cycleStart
            if curr in visited:
                cycleStart = curr
                return True

            visited.add(curr)

            for nei in graph[curr]:
                if nei == pare:
                    continue
                if dfs(nei, curr):
                    if cycleStart != -1:
                        cycle.add(curr)
                    if cycleStart == curr:
                        cycleStart = -1 
                        # this is two if not if-else, so when
                        # it goes back to the start of the circle
                        # first add the start, then set as -1
                    return True

            return False

        dfs(1, -1)
        
        for k, v in reversed(edges):
            if k in cycle and v in cycle:
                return [k, v]
        return []

