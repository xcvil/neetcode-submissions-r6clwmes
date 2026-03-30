class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        parent = {}
        weight = {}

        def find(x):
            if parent[x] != x:
                root = find(parent[x])
                weight[x] *= weight[parent[x]]
                parent[x] = root

            return parent[x]

        def union(a, b, val):
            pa = find(a)
            pb = find(b)
            if pa != pb:
                parent[pa] = pb
                weight[pa] = val * weight[b] / weight[a]

        for (a, b), v in zip(equations, values):
            for x in [a, b]:
                if x not in parent:
                    parent[x] = x
                    weight[x] = 1.0
            union(a, b, v)

        res = []
        for a, b in queries:
            if a not in parent or b not in parent:
                res.append(-1)
            elif find(a) != find(b):
                res.append(-1)
            else:
                res.append(weight[a] / weight[b])
        return res
        