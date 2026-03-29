class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        self.perimeter = 0
        move = [[1,0], [-1,0], [0,1], [0,-1]]

        def dfs(r, c):

            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                self.perimeter += 1
                return
            visited.add((r,c))

            for dr, dc in move:
                nr, nc = r + dr, c + dc
                if (nr, nc) not in visited:
                    dfs(nr, nc)

            return

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    dfs(r, c)
                    return self.perimeter
            