class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {i:set() for i in range(1, len(edges)+1)}

        for k, v in edges:
            graph[k].add(v)
            graph[v].add(k)

            visited = set()
            q = collections.deque()
            q.append((k, v))
            visited.add(k)

            while q:
                curr, pare = q.popleft()
                
                for nei in graph[curr]:
                    if nei == pare:
                        continue
                    if nei in visited:
                        return [k, v]
                    visited.add(nei)
                    q.append((nei, curr))