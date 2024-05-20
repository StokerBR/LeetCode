class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1 for _ in range(size)]
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
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort(key=lambda x: x[0])
        graph = UnionFind(n)
        
        for data in logs:
            graph.union(data[1], data[2])
            if graph.count == 1:
                return data[0]
    
        return -1
