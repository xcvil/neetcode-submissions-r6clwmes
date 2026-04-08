class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = [x for x in range(n)]
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return False
            if rank[ra] > rank[rb]:
                parent[rb] = ra
            elif rank[ra] < rank[rb]:
                parent[ra] = rb
            else:
                parent[ra] = rb
                rank[rb] += 1
            return True
        rootCount = n
        for k, v in edges:
            if union(k, v):
                rootCount -= 1
            else:
                return False

        return rootCount == 1