class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        direction = [[1,0], [-1,0], [0,1], [0,-1]]
        island = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):

            if (r<0 or r>=rows or c<0 or c>=cols or grid[r][c]=="0"):
                return
            
            grid[r][c] = "0"

            for dr, dc in direction:
                dfs(r+dr, c+dc)

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    island += 1
                
                dfs(r,c)

        return island