class Solution:
    def solve(self, board: List[List[str]]) -> None:
        move = [[1,0], [-1,0], [0,1], [0,-1]]
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r, c, component):
            # touch the boarder
            if (r < 0 or r >= rows or c < 0 or c >= cols):
                return True
            
            if (board[r][c] == 'X' or (r, c) in visited):
                return False

            visited.add((r, c))
            component.append((r, c))   

            touched = False
            for dr, dc in move:
                if dfs(r+dr, c+dc, component):
                    touched = True

            return touched

        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r, c) not in visited:
                    component = []
                    if not dfs(r, c, component):
                        for cr, cc in component:
                            board[cr][cc] = "X"


        