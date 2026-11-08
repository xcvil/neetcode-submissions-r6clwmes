class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if grid[i][j] != '1' or (i, j) in visited:   # 是水或已访问
                return
            visited.add((i, j))                    # 先标记再递归
            dfs(i + 1, j); dfs(i - 1, j)
            dfs(i, j + 1); dfs(i, j - 1)

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in visited:   # 两个条件都要
                    count += 1
                    dfs(i, j)
        return count