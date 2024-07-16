# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:                
        def lowest_common_acestor(node): 
            if not node or node.val in (startValue , destValue):
                return node 
            left, right = lowest_common_acestor(node.left), lowest_common_acestor(node.right)
            return node if left and right else left or right
        
        root = lowest_common_acestor(root)
        
        ps = pd = ""
        stack = [(root, "")]
        while stack: 
            node, path = stack.pop()
            if node.val == startValue:
                ps = path 
            if node.val == destValue:
                pd = path
            if node.left:
                stack.append((node.left, path + 'L'))
            if node.right:
                stack.append((node.right, path + 'R'))

        return 'U'*len(ps) + pd