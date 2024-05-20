class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        self.count = size

    def find(self, vert):
        if self.root[vert] == vert:
            return vert
        self.root[vert] = self.find(self.root[vert])
        return self.root[vert]
    
    def union(self, v1, v2):
        r1 = self.find(v1)
        r2 = self.find(v2)
        if r1 != r2:
            if self.rank[r1] > self.rank[r2]:
                self.root[r2] = r1
            elif self.rank[r1] < self.rank[r2]:
                self.root[r1] = r2
            else:
                self.root[r2] = r1
                self.rank[r1] += 1
            self.count -= 1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = UnionFind(n)

        for a, b in edges:
            graph.union(a, b)
        
        return graph.count