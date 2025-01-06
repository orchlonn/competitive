class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or grid[0]:
            return 0

        ROWS, COLS = len(grid), leng(grid[0])
        seen = set()
        island = 0

        def dfs(row, col):
            if (min(row, col) < 0 or
                (row, col) in seen or
                grid[row][col] == '0'
            ):
                return

            seen.add(row, col)
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dx, dy in directions:
                dfs(row + dx, col + dy)

        for r in range(grid):
            for c in range(grid[0]):
                if ((r, c) not in seen and grid[r][c] == '1'):
                    island += 1
                    dfs(r, c)
        
        return island