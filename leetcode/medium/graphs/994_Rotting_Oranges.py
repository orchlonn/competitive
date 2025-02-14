class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def isValid(row, col):
            return row in range(ROWS) and col in range(COLS)

        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        queue = deque()
        visit = set()
        ans = 0
        freshOranges = 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    queue.append((row, col, 0))
                    visit.add((row, col))
                if grid[row][col] == 1:
                    freshOranges += 1

        while queue:
            row, col, time = queue.popleft()
            ans = time
            for dx, dy in directions:
                next_row, next_col = row + dx, col + dy
                if ( isValid(next_row, next_col) and 
                    (next_row, next_col) not in visit and
                    grid[next_row][next_col] == 1
                ):
                    queue.append((next_row, next_col, time + 1))
                    visit.add((next_row, next_col))
                    freshOranges -= 1
        
        return ans if freshOranges == 0 else -1