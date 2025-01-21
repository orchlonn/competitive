class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        ans = 0

        def dfs(row, col):
            if (row not in range(ROWS) or
                col not in range(COLS) or
                (row, col) in visit or
                grid[row][col] == '0'
            ):
                return 
            
            visit.add((row, col))
            for dx, dy in directions:
                if (row + dx in range(ROWS) and col + dy in range(COLS) and grid[row + dx][col + dy] and (row + dx, col + dy) not in visit):
                    dfs(row + dx, col + dy)
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visit and grid[r][c] == '1':
                    ans += 1
                    dfs(r, c)
        
        return ans