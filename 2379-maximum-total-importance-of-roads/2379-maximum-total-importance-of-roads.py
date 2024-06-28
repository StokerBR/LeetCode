class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        conn = [0] * n
        for road in roads:
            conn[road[0]] += 1
            conn[road[1]] += 1

        conn.sort()
        res = 0
        cost = 1
        for con in conn:
            res += con * cost
            cost += 1
        return res