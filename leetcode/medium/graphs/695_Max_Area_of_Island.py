class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid and grid[0]:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        area = 0
        visit = set()

        def dfs(row, col):
            if (row not in range(ROWS) or
                col not in range(COLS) or
                (row, col) in visit or
                grid[row][col] == 0
            ):
                return 0
                
            visit.add((row, col))
            return (1 + dfs(row + 1, col) +
                        dfs(row - 1, col) + 
                        dfs(row, col + 1) + 
                        dfs(row, col - 1))
        
        for r in range(ROWS):
            for c in range(COLS):
                if ((r, c) not in visit and grid[r][c] == 1):
                    area = max(area, dfs(r, c))
        
        return area