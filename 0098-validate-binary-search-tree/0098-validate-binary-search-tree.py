# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, leftLimit, rightLimit):
            if not node:
                return True

            if leftLimit < node.val < rightLimit:
                return dfs(node.left, leftLimit, node.val) and dfs(node.right, node.val, rightLimit)
            else:
                return False

        return dfs(root, float('-inf'), float('inf'))