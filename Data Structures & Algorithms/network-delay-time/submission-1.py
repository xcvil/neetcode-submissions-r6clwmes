class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = collections.defaultdict(set)

        for u, v, t in times:
            graph[u].add((v, t))
        dist = {node: float("inf") for node in range(1, n + 1)}

        def dfs(node, length):
            if length >= dist[node]:
                return
            dist[node] = length
            for nei, t in graph[node]:
                dfs(nei, length+t)

        dfs(k, 0)
        res = max(dist.values())
        return res if res < float('inf') else -1

