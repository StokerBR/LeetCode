# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        trees = []

        def dfs(node):
            if not node.right and not node.left:
                return
            
            if node.left:
                dfs(node.left)
                if node.left.val in to_delete:
                    if node.left.left and node.left.left.val not in to_delete:
                        trees.append(node.left.left)
                    if node.left.right and node.left.right.val not in to_delete:
                        trees.append(node.left.right)
                    node.left = None
            
            if node.right:
                dfs(node.right)
                if node.right.val in to_delete:
                    if node.right.left and node.right.left.val not in to_delete:
                        trees.append(node.right.left)
                    if node.right.right and node.right.right.val not in to_delete:
                        trees.append(node.right.right)
                    node.right = None
        
        dfs(TreeNode(None, root))
        if root.val not in to_delete:
            trees.insert(0, root)
        return trees