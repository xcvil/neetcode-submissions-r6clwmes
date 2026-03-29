class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        move = [[0, 1], [0,-1], [1,0], [-1,0]]
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            if (r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0):
                return 0

            grid[r][c] = 0
            area = 1    
            for dr, dc in move:
                area += dfs(r+dr, c+dc)

            return area

        area = 0
        for r in range(rows):
            for c in range(cols):
                area = max(area, dfs(r, c))
        return area
