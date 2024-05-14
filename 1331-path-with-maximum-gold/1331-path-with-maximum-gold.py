class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(grid, i, j):
            curr = grid[i][j]
            maxGold = curr
            grid[i][j] = 0

            for next_i, next_j in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                if 0 <= next_i < len(grid) and 0 <= next_j < len(grid[0]) and grid[next_i][next_j] != 0:
                    maxGold = max(maxGold, curr+dfs(grid, next_i, next_j))

            grid[i][j] = curr
            return maxGold

        maxGold = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                maxGold = max(maxGold, dfs(grid, i, j))

        return maxGold