"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        hashmap = {node: Node(node.val)}
        q = deque()
        q.append(node)

        while q:
            cur = q.popleft()
            for nei in cur.neighbors:
                if nei not in hashmap:
                    hashmap[nei] = Node(nei.val)      # 第一次见到：克隆并登记
                    q.append(nei)                     # 入队，之后再处理它的邻居
                hashmap[cur].neighbors.append(hashmap[nei])   # 每条边都要连

        return hashmap[node]