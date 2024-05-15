class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        if grid[0][0] or grid[n-1][n-1]:
            return 0

        scores = [[float('inf')] * n for _ in range(n)]
        q = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    scores[i][j] = 0
                    q.append((i,j))

        while q:
            i, j = q.popleft()
            s = scores[i][j]

            for new_i, new_j in dirs:
                new_i += i
                new_j += j
                if 0 <= new_i < n and 0 <= new_j < n and scores[new_i][new_j] > s + 1:
                    scores[new_i][new_j] = s + 1
                    q.append((new_i, new_j))

        visited = set()
        pq = [(-scores[0][0], 0, 0)]

        while pq:
            safeness, i, j = heapq.heappop(pq)
            safeness = -safeness

            if i == n-1 and j == n-1:
                return safeness

            for new_i, new_j in dirs:
                new_i += i
                new_j += j
                if 0 <= new_i < n and 0 <= new_j < n and (new_i, new_j) not in visited:
                    s = min(safeness, scores[new_i][new_j])
                    heapq.heappush(pq, (-s, new_i, new_j))
                    visited.add((new_i, new_j))
        
        return -1
