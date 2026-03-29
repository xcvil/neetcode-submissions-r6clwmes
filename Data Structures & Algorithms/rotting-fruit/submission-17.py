class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        move = [[1,0], [-1,0], [0,1], [0,-1]]
        fresh = 0
        q = collections.deque()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append((row, col))
                if grid[row][col] == 1:
                    fresh += 1

        if fresh == 0:
            return 0
            
        time = 0
        while q:
            
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in move:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc))

            time += 1

            
        return time-1 if fresh == 0 else -1