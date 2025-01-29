class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        def isValid(row, col):
            return row in range(ROWS) and col in range(COLS)

        ROWS, COLS = len(grid), len(grid[0])
        queue = deque([(0, 0, 0, k)])
        visit = set((0, 0, k))
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        while queue:
            row, col, steps, remain = queue.popleft()
            if row == ROWS - 1 and col == COLS - 1:
                return steps

            for dx, dy in directions:
                next_row, next_col = row + dx, col + dy
                if isValid(next_row, next_col):
                    if (next_row, next_col, remain) not in visit and grid[next_row][next_col] == 0:
                        queue.append((next_row, next_col, steps + 1, remain))
                        visit.add((next_row, next_col, remain))

                    # should be obstacles
                    elif remain and (next_row, next_col, remain - 1) not in visit:
                        queue.append((next_row, next_col, steps + 1, remain - 1))
                        visit.add((next_row, next_col, remain - 1))
        
        return -1
