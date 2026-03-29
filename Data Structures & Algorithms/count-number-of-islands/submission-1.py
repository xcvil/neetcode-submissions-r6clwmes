class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        move = [[1,0], [-1,0], [0,1], [0,-1]]
        island = 0
        

        def bfs(r,c):
            q = collections.deque()
            grid[r][c] = "0"
            q.append((r,c))

            while q:
                row,col = q.popleft()
                for dr, dc in move:
                    nr, nc = row+dr, col+dc
                    if (nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] == "0"):
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = "0"

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r,c)
                    island += 1
        return island
