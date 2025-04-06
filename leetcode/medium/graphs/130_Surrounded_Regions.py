class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c):
            if (r not in range(ROWS) or c not in range(COLS) or board[r][c] != "O"):
                return 
            
            board[r][c] = "T"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for row in range(ROWS):
            for col in range(COLS):
                if (board[row][col] == "O" and 
                    (row in [0, ROWS - 1] or col in [0, COLS - 1])):
                    dfs(row, col)
        
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "O":
                    board[row][col] = "X"

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "T":
                    board[row][col] = "O"