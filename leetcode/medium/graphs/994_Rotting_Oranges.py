class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        queue = deque()
        cntr, fresh = 0, 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r, c))

        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dx, dy in directions:
                    row, col = r + dx, c + dy
                    if ((row) in range(ROWS) and 
                        (col) in range(COLS) and
                        grid[row][col] == 1
                    ):
                        fresh -= 1
                        queue.append((row, col))
                        grid[row][col] = 2
            cntr += 1
        return cntr if fresh == 0 else -1