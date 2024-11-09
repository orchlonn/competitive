class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        island = 0
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()

        def dfs(row, col):
            if( row not in range(ROWS)
                or col not in range(COLS)
                or grid[row][col] == "0"
                or (row, col) in seen
            ):
                return
            
            seen.add((row, col))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dx, dy in directions:
                dfs(row + dx, col + dy)


        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in seen and grid[r][c] == "1":
                    island += 1
                    dfs(r, c)
        
        return island