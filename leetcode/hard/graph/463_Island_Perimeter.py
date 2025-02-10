class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def dfs(row, col):
            if (row not in range(ROWS) or
                col not in range(COLS) or
                grid[row][col] == 0
            ):
                return 1
            
            if (row, col) in visit:
                return 0
            
            visit.add((row, col))

            perim = 0
            for dx, dy in directions:
                next_row, next_col = row + dx, col + dy
                perim += dfs(next_row, next_col)
            
            return perim
            
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    return dfs(row, col)