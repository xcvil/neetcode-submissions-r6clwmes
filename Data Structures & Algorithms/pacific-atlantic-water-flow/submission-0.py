class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # pacifi r<0 or c<0
        # atlantic r>=rows or c>=cols
        # p, and a
        # BFS
        move = [[1,0], [-1,0], [0,1], [0,-1]]
        rows, cols = len(heights), len(heights[0])

        def bfs(starts):
            visit = set(starts)
            q = collections.deque(visit)

            while q:
                r, c = q.popleft()
                for dr, dc in move:
                    nr, nc = r+dr, c+dc
                    if (nr < 0 or nr >= rows or nc < 0 or nc >= cols or heights[nr][nc] < heights[r][c] or (nr, nc) in visit):
                        continue
                    visit.add((nr, nc))
                    q.append((nr, nc))

            return visit
        
        pac_starts = [(0, c) for c in range(cols)] + [(r, 0) for r in range(rows)]
        alt_starts = [(rows-1, c) for c in range(cols)] + [(r, cols-1) for r in range(rows)]

        return list(bfs(pac_starts) & bfs(alt_starts))

        