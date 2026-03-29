class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        move = [[1,0], [-1,0], [0,1], [0,-1]]

        def dfs(r, c):

            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:

                return 1
            visited.add((r,c))
            perimeter = 0
            for dr, dc in move:
                nr, nc = r + dr, c + dc
                if (nr, nc) not in visited:
                    perimeter += dfs(nr, nc)

            return perimeter

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    
                    return dfs(r, c)
            