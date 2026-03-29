# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True
        def dfs(node):
            if not node:
                return 0

            lHeight = 1 + dfs(node.left)
            rHeight = 1 + dfs(node.right)

            if abs(lHeight-rHeight) > 1:
                self.res = False
            return max(lHeight, rHeight)

        dfs(root)
        return self.res
