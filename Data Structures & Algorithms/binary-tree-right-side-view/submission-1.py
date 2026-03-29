# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()
        res = []
        q.append(root)

        while q:
            isRight = False
            lenQ = len(q)

            for _ in range(lenQ):
                node = q.popleft()
                if node:
                    if not isRight:
                        res.append(node.val)
                        isRight = True
                    q.append(node.right)
                    q.append(node.left)
            
        return res