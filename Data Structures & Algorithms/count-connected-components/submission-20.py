class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [x for x in range(n)]
        rank = [1] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            roota, rootb = find(a), find(b)

            if roota != rootb:
                if rank[roota] > rank[rootb]:
                    parent[rootb] = roota
                elif rank[roota] < rank[rootb]:
                    parent[roota] = rootb
                else:
                    parent[roota] = rootb
                    rank[roota] += 1
                # return True

        for k, v in edges:
            union(k, v)

        groups = [find(x) for x in range(n)]

        return len(set(groups))