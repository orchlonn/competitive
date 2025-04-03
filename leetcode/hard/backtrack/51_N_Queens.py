class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for i in range(n)]
        posDiag = set() # r + c
        negDiag = set() # r - c
        cols = set()

        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return
            
            for c in range(n):
                if c in cols or (r + c) in posDiag or (r - c) in negDiag or board[r][c] == "Q":
                    continue 
                    
                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."
        
        backtrack(0)
        return res
        
# Time complexity: O(N!)
# Space complexity: O(N^2) for board + O(N) for backtracking.