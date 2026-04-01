class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return[0]

        graph = collections.defaultdict(set)
        for k, v in edges:
            graph[k].add(v)
            graph[v].add(k)

        down1 = [0] * n
        down2 = [0] * n
        up = [0] * n
        down1_to_child = [-1] * n

        def dfs_down(node, parent):
            for nei in graph[node]:
                if nei == parent:
                    continue
                dfs_down(nei, node)
                depth = 1 + down1[nei]

                if depth >= down1[node]:
                    down2[node] = down1[node]
                    down1[node] = depth
                    down1_to_child[node] = nei
                elif depth > down2[node]:
                    down2[node] = depth

        def dfs_up(node, parent):
            for nei in graph[node]:
                if nei == parent:
                    continue

                if nei == down1_to_child[node]:
                    up[nei] = 1 + max(up[node], down2[node])
                else:
                    up[nei] = 1 + max(up[node], down1[node])

                dfs_up(nei, node)

        dfs_down(0, -1)
        dfs_up(0, -1)

        heights = [max(up[i], down1[i]) for i in range(n)]
        minHeight = min(heights)
        return [i for i in range(n) if heights[i] == minHeight]