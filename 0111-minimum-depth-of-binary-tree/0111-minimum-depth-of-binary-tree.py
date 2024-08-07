# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0

            if not node.left and not node.right:
                return 1

            leftDepth = dfs(node.left)
            rightDepth = dfs(node.right)
            if not node.left:
                return 1 + rightDepth
            if not node.right:
                return 1 + leftDepth

            return min(leftDepth, rightDepth) + 1
        
        return dfs(root)