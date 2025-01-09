class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        fresh, counter = 0, 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r, c))
        
        while queue and fresh > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dx, dy in directions:
                    if r + dx in range(ROWS) and c + dy in range(COLS) and grid[r + dx][c + dy] == 1:
                        grid[r + dx][c + dy] = 2
                        fresh -= 1
                        queue.append((r + dx, c + dy))


            counter += 1
        return counter if fresh == 0 else -1