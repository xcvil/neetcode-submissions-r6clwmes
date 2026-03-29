class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        move = [[1,0], [-1,0], [0,1], [0,-1]]
        pac = set()
        alt = set()


        def dfs(r, c, visited, preHeight):

            if (r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited or heights[r][c] < preHeight):
                return
            
            visited.add((r, c))
            for dr, dc in move:
                dfs(r + dr, c + dc, visited, heights[r][c])

        for r in range(rows):
            dfs(r, 0, pac, 0)
            dfs(r, cols-1, alt, 0)
        for c in range(cols):
            dfs(0, c, pac, 0)
            dfs(rows-1, c, alt, 0)

        return list(pac & alt)

