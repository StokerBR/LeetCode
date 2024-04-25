# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs_invert(node):
            if not node:
                return

            tmp = node.left
            node.left = node.right
            node.right = tmp

            dfs_invert(node.left)
            dfs_invert(node.right)
        dfs_invert(root)
        return root