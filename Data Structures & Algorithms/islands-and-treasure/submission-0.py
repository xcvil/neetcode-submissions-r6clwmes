class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        move = [[1,0], [-1,0], [0,1], [0,-1]]
        rows = len(grid)
        cols = len(grid[0])
        q = collections.deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))

        while q:
            row, col = q.popleft()
            for dr, dc in move:
                nr, nc = row+dr, col+dc
                if (nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != 2147483647):
                    continue
                grid[nr][nc] = grid[row][col] + 1
                q.append((nr,nc))