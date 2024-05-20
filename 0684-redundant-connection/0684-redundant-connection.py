class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        root = [i for i in range(len(edges)+1)]

        def find(v):
            if root[v] == v:
                return v
            root[v] = find(root[v])
            return root[v]

        def union(v1, v2):
            r1 = find(v1)
            r2 = find(v2)

            if r1 == r2:
                return True
            else:
                root[r2] = r1
                return False
        
        for u, v in edges:
            if union(u, v):
                return [u, v]