class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            if grid[r][0] == 0:
                for c in range(cols):
                    grid[r][c] = 0 if grid[r][c] else 1

        for c in range(cols):
            onesCount = 0
            for r in range(rows):
                onesCount += grid[r][c]
            if onesCount < rows - onesCount:
                for r in range(rows):
                    grid[r][c] = 0 if grid[r][c] else 1
        
        res = 0
        for r in range(rows):
            for c in range(cols):
                res += grid[r][c] << (cols-1-c)
        
        return res