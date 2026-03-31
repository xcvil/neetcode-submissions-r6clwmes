class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # down1[i]: 最大向下深度
        # down2[i]: 次大向下深度
        # down1_child[i]: 最大深度来自哪个孩子
        down1 = [0] * n
        down2 = [0] * n
        down1_child = [-1] * n
        up = [0] * n
        
        # === 第一遍DFS：算向下深度 ===
        def dfs_down(node, parent):
            for nei in graph[node]:
                if nei == parent:
                    continue
                dfs_down(nei, node)
                depth = 1 + down1[nei]
                if depth >= down1[node]:        # 注意 >= ，更新最大和次大
                    down2[node] = down1[node]
                    down1[node] = depth
                    down1_child[node] = nei
                elif depth > down2[node]:
                    down2[node] = depth
        
        # === 第二遍DFS：算向上深度 ===
        def dfs_up(node, parent):
            for nei in graph[node]:
                if nei == parent:
                    continue
                # nei往上走 = 1 + max(node往上, node往下但不经过nei)
                if down1_child[node] == nei:
                    # nei是node最大深度的来源，用次大
                    up[nei] = 1 + max(up[node], down2[node])
                else:
                    up[nei] = 1 + max(up[node], down1[node])
                dfs_up(nei, node)
        
        dfs_down(0, -1)
        dfs_up(0, -1)
        
        # 每个节点作为根的树高 = max(down1[i], up[i])
        heights = [max(down1[i], up[i]) for i in range(n)]
        min_h = min(heights)
        return [i for i in range(n) if heights[i] == min_h]