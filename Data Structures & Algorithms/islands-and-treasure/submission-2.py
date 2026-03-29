class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        move = [[1,0], [-1,0], [0,1], [0,-1]]
        q = collections.deque()
        rows, cols =  len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))

        while q:
            r, c = q.popleft()
            for dr, dc in move:
                nr, nc = r + dr, c + dc

                if (nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != 2147483647):
                    continue

                grid[nr][nc] = grid[r][c] + 1

                q.append((nr, nc))
        