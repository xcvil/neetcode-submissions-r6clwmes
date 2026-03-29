class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        move = [[0,1], [0,-1], [1,0], [-1,0]]
        minT = 0
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1       # 记录新鲜橘子数量

        if fresh == 0:
            return 0                 # 没有新鲜橘子，直接返回 0

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in move:
                    nr, nc = r+dr, c+dc
                    if (nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != 1):
                        continue
                    grid[nr][nc] = 2
                    q.append((nr, nc))
                    fresh -= 1
            minT += 1

        return minT-1 if fresh == 0 else -1
    