class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        island = 0
        rows, cols = len(grid), len(grid[0])
        seen = set()

        def dfs(row, col):
            if (row not in range(rows) or
                col not in range(cols) or
                grid[row][col] == '0' or
                (row, col) in seen
            ):
                return 
            
            seen.add((row, col))
            directions = [[0,1], [0, -1], [1, 0], [-1, 0]]
            for dx, dy in directions:
                dfs(row + dx, col + dy)
        
        for r in range(rows):
            for c in range(cols):
                if ((r, c) not in seen and grid[r][c] == '1'):
                    island += 1
                    dfs(r, c)
        
        return island 