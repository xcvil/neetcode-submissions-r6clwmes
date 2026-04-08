# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(node: Optional[TreeNode]):

            if not node:
                return 0

            lHeight = dfs(node.left)
            rHeight = dfs(node.right)

            self.res = max(self.res, lHeight+rHeight)

            return 1 + max(lHeight, rHeight)

        dfs(root)
        return self.res
