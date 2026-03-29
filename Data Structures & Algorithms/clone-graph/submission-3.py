"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hashMap = {}
        if not node:
            return 

        def dfs(node):
            if node in hashMap:
                return hashMap[node]

            curr = Node(val = node.val)
            hashMap[node] = curr
            for nei in node.neighbors:
                curr.neighbors.append(dfs(nei))

            return curr

        # dfs(node)
        # return hashMap[node]
        return dfs(node) if node else None



