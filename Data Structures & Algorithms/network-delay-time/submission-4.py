class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        import heapq

        graph = collections.defaultdict(list)

        for u, v, t in times:
            graph[u].append((v, t))
        dist = {node: float("inf") for node in range(1, n + 1)}

        heap = [(0, k)]
        dist[k] = 0
        while heap:
            cost, u = heapq.heappop(heap)
            if cost > dist[u]: continue

            for v, w in graph[u]:
                new_dist = w + cost
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(heap, (new_dist, v)) 
        res = max(dist.values())
        return res if res < float('inf') else -1  

