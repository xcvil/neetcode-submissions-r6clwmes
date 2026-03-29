class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        island = 0
        move = [[1,0], [-1,0], [0,1], [0,-1]]

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))

            while q:
                row, col = q.popleft()
                if grid[row][col] == "1":
                    grid[row][col] = "0"
                    for dr, dc in move:
                        nr, nc = row + dr, col + dc
                        if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                            continue
                        q.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    island += 1
                    bfs(r, c)

        return island
            
        
        