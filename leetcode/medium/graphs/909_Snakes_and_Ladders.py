class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        length = len(board)
        board.reverse()
        
        def intToPos(square):
            row = (square - 1) // length
            col = (square - 1) % length
            if row % 2:
                col = length - 1 - col
            return [row, col]    
        
        queue = deque([(1, 1)])
        visit = set()
        
        while queue:
            square, steps = queue.popleft()
            
            for i in range(1, 7):
                nextSquare = square + i
                row, col = intToPos(nextSquare)
                
                if board[row][col] != -1:
                    nextSquare = board[row][col]
                
                if nextSquare == length * length:
                    return steps
                
                if nextSquare not in visit:
                    visit.add((nextSquare))
                    queue.append((nextSquare, steps + 1))
                    
        return -1