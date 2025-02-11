class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def dfs(r, c):
            if (r not in range(ROWS) or
                c not in range(COLS) or
                (r, c) in visit or
                not grid[r][c] 
            ):
                return 0
            
            visit.add((r, c))
            res = 1
            for dx, dy in directions:
                res += dfs(r + dx, c + dy)
            
            return res

        land, borderLand = 0, 0

        for r in range(ROWS):
            for c in range(COLS):
                land += grid[r][c]
                if ((r, c) not in visit and grid[r][c] and
                    (r in [0, ROWS - 1] or c in [0, COLS - 1])
                ):
                    borderLand += dfs(r, c)

        return land - borderLand