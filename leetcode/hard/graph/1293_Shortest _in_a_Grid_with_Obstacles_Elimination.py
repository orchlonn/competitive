class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        def isValid(row, col):
            return row in range(ROWS) and col in range(COLS)

        ROWS, COLS = len(grid), len(grid[0])
        visit = set((0, 0, k))
        queue = deque([(0, 0, k, 0)]) # row, col, steps, k
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        while queue:
            row, col, remain, steps = queue.popleft()
                
            if row == ROWS - 1 and col == COLS - 1:
                return steps
            
            for dx, dy in directions:
                next_row, next_col = row + dy, col + dx
                if isValid(next_row, next_col):
                    if grid[next_row][next_col] == 0:
                        if (next_row, next_col, remain) not in visit:
                            visit.add((next_row, next_col, remain))
                            queue.append((next_row, next_col, remain, steps + 1))
                    # otherwise, it is an obstacle and we can only pass if we have remaining removals
                    elif remain and (next_row, next_col, remain - 1) not in visit:
                        visit.add((next_row, next_col, remain - 1))
                        queue.append((next_row, next_col, remain - 1, steps + 1))

        return -1
        

