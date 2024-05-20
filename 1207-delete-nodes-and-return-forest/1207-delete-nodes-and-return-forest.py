# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        delete = set(to_delete)
        res = []
        def dfs(node):
            if not node:
                return

            dfs(node.left)
            dfs(node.right)

            if node.left and node.left.val in delete:
                if node.left.left:
                    res.append(node.left.left)
                if node.left.right:
                    res.append(node.left.right)
                node.left = None
            if node.right and node.right.val in delete:
                if node.right.left:
                    res.append(node.right.left)
                if node.right.right:
                    res.append(node.right.right)
                node.right = None

        dfs(root)
        if root.val not in delete:
            res.append(root)
        else:
            if root.right:
                res.append(root.right)
            if root.left:
                res.append(root.left)
        return res