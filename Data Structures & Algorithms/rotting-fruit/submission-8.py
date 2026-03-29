class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        move = [[1,0], [-1,0], [0,1], [0,-1]]
        q = collections.deque()
        rows, cols = len(grid), len(grid[0])
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))

                if grid[r][c] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        mint = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in move:
                    nr, nc = r + dr, c + dc
                    if (nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != 1):
                        continue
                    grid[nr][nc] = 2
                    q.append((nr, nc))
                    fresh -= 1

            mint += 1
        
        return mint-1 if fresh == 0 else -1