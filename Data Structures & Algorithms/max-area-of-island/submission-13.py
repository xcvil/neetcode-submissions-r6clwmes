class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        move = [[0, 1], [0,-1], [1,0], [-1,0]]
        rows = len(grid)
        cols = len(grid[0])

        def bfs(r, c):
            if grid[r][c] == 0:
                return 0
            q = collections.deque()
            q.append((r, c))
            grid[r][c] = 0
            area = 1

            while q:
                row, col = q.popleft()
                for dr, dc in move:
                    nr, nc = row + dr, col + dc
                    if (nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] == 0):
                        continue
                    area += 1
                    q.append((nr, nc))
                    grid[nr][nc] = 0

            return area

        maxArea = 0
        for r in range(rows):
            for c in range(cols):
                maxArea = max(maxArea, bfs(r, c))
        return maxArea
        