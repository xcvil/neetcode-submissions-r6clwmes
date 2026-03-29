class Solution:
    def solve(self, board: List[List[str]]) -> None:
        move = [[1,0], [-1,0], [0,1], [0,-1]]
        rows, cols = len(board), len(board[0])


        def dfs(r, c):
            if (r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] == 'X' or board[r][c] == "#"):
                return
            
            board[r][c] = "#"
            
            for dr, dc in move:
                nr, nc = r + dr, c + dc
                dfs(nr, nc)

        for c in range(cols):
            dfs(0, c)
            dfs(rows-1, c)

        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols-1)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "#":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"