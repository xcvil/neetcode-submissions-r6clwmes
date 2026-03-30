class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        graph = collections.defaultdict(set)

        for k, v in edges:
            graph[k].add(v)
            graph[v].add(k)

        def dfs(node):
            if node in visited:
                return 0
            visited.add(node)

            height = 0

            for nei in graph[node]:
                height = max(height, dfs(nei))

            return height + 1

        minHeight = float('inf')
        res = []
        for i in range(n):
            visited = set()
            currHeight = dfs(i)
            if currHeight < minHeight:
                res = [i]
                minHeight = currHeight
            elif currHeight == minHeight:
                res.append(i)
            else:
                continue

        return res


