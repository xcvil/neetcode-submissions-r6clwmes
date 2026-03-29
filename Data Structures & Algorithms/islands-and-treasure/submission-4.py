class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        move = [[1,0], [-1,0], [0,1], [0,-1]]
        rows = len(grid)
        cols = len(grid[0])

        q = collections.deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    q.append((row, col))

        while q:
            r, c = q.popleft()
            for dr, dc in move:
                nr, nc = r + dr, c + dc
                # if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] == -1:
                #     continue
                # if grid[nr][nc] == 2147483647:
                #     grid[nr][nc] = 1 + grid[r][c]
                #     q.append((nr, nc))
                if (nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != 2147483647):
                    continue
                grid[nr][nc] = 1 + grid[r][c]
                q.append((nr, nc))

        