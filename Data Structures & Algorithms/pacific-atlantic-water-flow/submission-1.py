class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # pacifi r<0 or c<0
        # atlantic r>=rows or c>=cols
        # p, and a
        # DFS

        move = [[1,0], [-1,0], [0,1], [0,-1]]
        rows, cols = len(heights), len(heights[0])
        pac, alt = set(), set()

        def dfs(r, c, visited, preH):
            if (r < 0 or r >= rows or c < 0 or c >= cols or heights[r][c] < preH or (r, c) in visited):
                return

            visited.add((r,c))

            for dr, dc in move:
                dfs(r+dr, c+dc, visited, heights[r][c])

        for c in range(cols):
            dfs(0, c, pac, 0)
            dfs(rows-1, c, alt, 0)

        for r in range(rows):
            dfs(r, 0, pac, 0)
            dfs(r, cols-1, alt, 0)

        return list(pac & alt)

        