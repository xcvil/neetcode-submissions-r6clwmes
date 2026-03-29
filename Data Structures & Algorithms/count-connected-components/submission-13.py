class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: set() for i in range(n)}

        for k, v in edges:
            graph[k].add(v)
            graph[v].add(k)

        visited = set()

        def bfs(node): # E
            visited.add(node)
            q = collections.deque()
            q.append(node)
            while q:
                node = q.popleft()
                for nei in graph[node]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)

        
        connected = 0

        for i in range(n): # V
            if i not in visited:
                bfs(i)
                connected += 1
        return connected
        