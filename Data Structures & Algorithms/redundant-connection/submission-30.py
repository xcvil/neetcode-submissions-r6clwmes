class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {x: x for x in range(len(edges)+1)}
        rank =  {x: 1 for x in range(len(edges)+1)}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            roota, rootb = find(a), find(b)
            if roota == rootb:
                return False

            if rank[roota] > rank[rootb]:
                parent[rootb] = roota
            elif rank[roota] < rank[rootb]:
                parent[roota] = rootb
            else:
                parent[roota] = rootb
                rank[rootb] += 1
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
        return []
        
        
