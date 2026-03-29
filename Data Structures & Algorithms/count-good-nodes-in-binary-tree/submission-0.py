# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = collections.deque()
        q_max = collections.deque()
        res = 0

        q.append(root)
        q_max.append(float('-inf'))

        while q:

            lenQ = len(q)
            for _ in range(lenQ):
                node = q.popleft()
                node_max = q_max.popleft()

                if node: 
                    if node.val >= node_max:
                        res += 1
                        node_max = node.val
                    
                    q.append(node.left)
                    q.append(node.right)
                    q_max.append(node_max)
                    q_max.append(node_max)

        return res

            