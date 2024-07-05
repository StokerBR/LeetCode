class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0

        for i in range(1, len(costs)):
            mins = heapq.nsmallest(2, costs[i - 1])
            for j in range(len(costs[0])):
                costs[i][j] += mins[1] if costs[i - 1][j] == mins[0] else mins[0]
                
        return min(costs[-1])