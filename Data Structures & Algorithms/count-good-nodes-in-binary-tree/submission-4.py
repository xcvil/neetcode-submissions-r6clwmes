# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        q = collections.deque()
        max_q = collections.deque()
        q.append(root)
        max_q.append(float('-inf'))

        while q:
            lenQ = len(q)
            for _ in range(lenQ):
                node = q.popleft()
                max_val = max_q.popleft()
                if node:
                    if node.val >= max_val:
                        res += 1
                        max_val = node.val

                    q.append(node.left)
                    q.append(node.right)
                    max_q.append(max_val)
                    max_q.append(max_val)
        return res

        