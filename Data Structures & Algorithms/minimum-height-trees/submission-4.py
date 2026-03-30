class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        graph = collections.defaultdict(set)

        for k, v in edges:
            graph[k].add(v)
            graph[v].add(k)

        def dfs(node, paren):

            height = 0

            for nei in graph[node]:
                if nei != paren:
                    height = max(height, 1+dfs(nei, node))

            return height

        minHeight = float('inf')
        res = []
        for i in range(n):
            currHeight = dfs(i, -1)
            if currHeight < minHeight:
                res = [i]
                minHeight = currHeight
            elif currHeight == minHeight:
                res.append(i)
            else:
                continue

        return res


