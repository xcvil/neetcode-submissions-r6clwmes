class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        subset = [["."]*n for _ in range(n)]

        def check(r, c):
                for i in range(r):
                    if subset[i][c] == 'Q':
                        return False
                for i in range(1, r+1):
                    if c-i >= 0 and subset[r-i][c-i] == 'Q':
                        return False
                    if c+i < n and  subset[r-i][c+i] == 'Q':
                        return False

                return True

        def dfs(r):
            

            if r == n: 
                res.append(["".join(s) for s in subset])
                return
            
            for c in range(n):
                
                # if [subset[row][c] for row in range(r)] == ["."]*r and check(r,c):
                if check(r,c):
                    subset[r][c] = 'Q'
                    dfs(r+1)
                    subset[r][c] = '.'

        dfs(0)
        return res