class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # 0:[1,2,3,4]
        # 1:[0,4]
        # 2:[0]
        # 3:[0]
        # 4:[0,1]
        if len(edges) == 0:
            return True
        graph = {i: set() for i in range(n)}
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        visited = set()

        def dfs(curr, parent):
            visited.add(curr)
            for nei in graph[curr]:
                if nei == parent:
                    continue
                if nei in visited:
                    return False
                if not dfs(nei, curr):
                    return False

            return True

        if not dfs(0,-1):
            return False
        return len(visited) == n

        

