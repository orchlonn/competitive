class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(r, c, i):
            if len(word) == i:
                return True

            if (r not in range(ROWS) or
                c not in range(COLS) or
                (r, c) in visit or
                board[r][c] != word[i]
            ):
                return False
            
            visit.add((r, c))
            res = ( backtrack(r + 1, c, i + 1) or 
                    backtrack(r - 1, c, i + 1) or 
                    backtrack(r, c + 1, i + 1) or 
                    backtrack(r, c - 1, i + 1))
            visit.remove((r, c))
            
            return res
        
        visit = set()
        ROWS, COLS = len(board), len(board[0])

        for row in range(ROWS):
            for col in range(COLS):
                if backtrack(row, col, 0): return True

        return False
# Time complexity: O(N * M * 4^N)
# Space complexity: O(N * M)