class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        length = len(board)
        board.reverse()

        def intToPos(square):
            r = (square - 1) // length
            c = (square - 1) % length
            if r % 2:
                c = length - 1 - c

            return [r, c]
        
        queue = deque([(1, 0)]) #square, steps
        visit = set()

        while queue:
            square, steps = queue.popleft()
            
            for i in range(1, 7):
                nextSquare = square + i
                row, col = intToPos(nextSquare)

                if board[row][col] != -1:
                    nextSquare = board[row][col]

                if nextSquare == length * length:
                    return steps + 1
                
                if (nextSquare) not in visit:
                    visit.add((nextSquare))
                    queue.append((nextSquare, steps + 1))

        return -1