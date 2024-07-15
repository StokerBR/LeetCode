# Definition for a binarc tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        root, n = -1, len(descriptions)
        parent = {}
        node = {}

        for p, c, l in descriptions:
            if p not in node:
                node[p] = TreeNode(p)
                if p not in parent:
                    root = p
            if c not in node:
                node[c] = TreeNode(c)
            parent[c] = p
            if l:
                node[p].left = node[c]
            else:
                node[p].right = node[c]

        while root in parent:
            root = parent[root]

        return node[root]
        