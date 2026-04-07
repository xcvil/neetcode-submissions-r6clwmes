class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(set)
        for k, v in edges:
            graph[k].add(v)
            graph[v].add(k)

        def dfs(start):
            if start in visited:
                return
            
            visited.add(start)

            for nei in graph[start]:
                dfs(nei)
            
            return

        visited = set()
        res = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1
        return res
