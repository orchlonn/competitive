class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        def isValid(row, col):
            return row in range(ROWS) and col in range(COLS)
            
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        queue = deque([(0, 0, 0, k)]) # row, col, steps, remainings
        visit = set((0, 0, k)) # row, col, remainings
        
        while queue:
            row, col, steps, remaining = queue.popleft()
            
            # base case 1: 
            if row == ROWS - 1 and col == COLS - 1:
                return steps
            
            for dx, dy in directions:
                next_row, next_col = row + dx, col + dy
                if isValid(next_row, next_col):
                    if (grid[next_row][next_col] == 0 and (next_row, next_col, remaining) not in visit):
                        queue.append((next_row, next_col, steps + 1, remaining))
                        visit.add((next_row, next_col, remaining))
                        
                    elif remaining and (next_row, next_col, remaining - 1) not in visit:
                        queue.append((next_row, next_col, steps + 1, remaining - 1))
                        visit.add((next_row, next_col, remaining - 1))
                        

        return -1