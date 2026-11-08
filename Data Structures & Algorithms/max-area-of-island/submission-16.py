class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        visited = set()
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            if grid[i][j] != 1 or (i, j) in visited:
                return 0
            area = 1
            visited.add((i, j))
            area += dfs(i, j + 1)
            area += dfs(i, j - 1)
            area += dfs(i - 1, j)
            area += dfs(i + 1, j)
            return area

        maxA = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    maxA = max(maxA, dfs(i, j))

        return maxA