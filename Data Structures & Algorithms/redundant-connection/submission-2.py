class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {i:set() for i in range(1, len(edges)+1)}

        for k, v in edges:
            graph[k].add(v)
            graph[v].add(k)

            visited = set()
            q = collections.deque()
            q.append((k, v))

            while q:
                curr, pare = q.popleft()
                visited.add(curr)
                for nei in graph[curr]:
                    if nei == pare:
                        continue
                    if nei in visited:
                        print(nei)
                        return [k, v]
                    q.append((nei, curr))