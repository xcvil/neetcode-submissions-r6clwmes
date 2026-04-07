class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [x for x in range(n)]
        rank = [1] * n
        count = n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            nonlocal count
            roota, rootb = find(a), find(b)

            if roota == rootb:
                return
            else:
                if rank[roota] > rank[rootb]:
                    parent[rootb] = roota
                elif rank[roota] < rank[rootb]:
                    parent[roota] = rootb
                else:
                    parent[roota] = rootb
                    rank[rootb] += 1
                count -= 1
                # return True

        for k, v in edges:
            union(k, v)

        return count