class Solution:
    def findRedundantConnection(self, edges):
        n = len(edges)
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        cycle = set()
        cycleStart = -1

        def dfs(node, par):
            nonlocal cycleStart
            if node in visited:
                cycleStart = node        # 环的起点
                return True
            visited.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                if dfs(nei, node):
                    if cycleStart != -1:  # 还在环上，收集
                        cycle.add(node)
                    if node == cycleStart: # 回到起点，停止
                        cycleStart = -1
                    return True
            return False

        dfs(1, -1)

        for u, v in reversed(edges):     # 从后往前
            if u in cycle and v in cycle:
                return [u, v]
        return []