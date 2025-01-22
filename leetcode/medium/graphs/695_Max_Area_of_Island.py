class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()
        ans = 0
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def dfs(row, col):
            if (row not in range(ROWS) or
                col not in range(COLS) or
                (row, col) in seen or
                grid[row][col] == 0 
            ):
                return 0
            
            seen.add((row, col))
            return (1 + dfs(row + 1, col) + 
                        dfs(row - 1, col) + 
                        dfs(row, col + 1) +
                        dfs(row, col - 1))
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in seen:
                    ans = max(ans, dfs(r, c))
        
        return ans