class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque
        count = 0
        q = deque()
        visited = set()

        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in visited:
                    count += 1
                    q.append((i, j))
                    visited.add((i, j))
                    while q:
                        x, y = q.popleft()
                        for dx, dy in ((1,0), (-1,0), (0,1), (0,-1)):
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1' and (nx, ny) not in visited:
                                q.append((nx, ny))
                                visited.add((nx, ny))

        return count