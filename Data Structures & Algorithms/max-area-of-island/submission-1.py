class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        self.maxA = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if (r<0 or r>=rows or c<0 or c>=cols or grid[r][c]==0):
                return 0

            grid[r][c] = 0

            area = 1
            for dr, dc in directions:
                area += dfs(r+dr, c+dc)
            
            self.maxA = max(self.maxA, area)

            return area

        for r in range(rows):
            for c in range(cols):
                dfs(r,c)

        return self.maxA
        