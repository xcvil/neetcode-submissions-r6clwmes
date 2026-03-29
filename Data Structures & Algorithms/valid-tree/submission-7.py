class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
            
        graph = {i: set() for i in range(n)}
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        visited = set()
        q = collections.deque()
        q.append((0,-1))
        visited.add(0)

        while q:
            curr, pare = q.popleft()
            for nei in graph[curr]:
                if nei == pare:
                    continue
                if nei in visited:
                    return False
                visited.add(nei)
                q.append((nei, curr))

        return len(visited) == n
        