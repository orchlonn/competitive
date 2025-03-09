class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def valid(row, column):
            return 0 <= row <= m and 0 <= column <= n:
        
        def backtrack(row, col, i, seen):
            if i == len(word):
                return True
            
            for dx, dy in directions:
                next_row, next_col = row + dy, col + dx
                

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m = len(board[0])
        n = len(board)

