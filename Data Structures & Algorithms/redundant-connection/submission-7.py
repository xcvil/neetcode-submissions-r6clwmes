class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {i:set() for i in range(1, len(edges)+1)}

        def dfs(start, end):
            if start == end:
                return True
            visited.add(start)
            for nei in graph[start]:
                if nei not in visited:
                    if dfs(nei, end):
                        return True
        
            

        for k, v in edges:
            visited = set()

            if not dfs(k, v):

                graph[k].add(v)
                graph[v].add(k)
            else:
                return [k, v]