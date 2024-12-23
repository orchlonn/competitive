class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        rows, cols = len(grid), len(grid[0])
        ans = 0

        def dfs(r, c):
            if( r not in range(rows)
                or c not in range(cols)
                or (r, c) in seen
                or grid[r][c] == 0
            ):
                return 0
    
            seen.add((r, c))
            return (1 + dfs(r + 1, c) + 
                        dfs(r - 1, c) + 
                        dfs(r, c + 1) + 
                        dfs(r, c - 1))

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in seen and grid[r][c] == 1:
                    ans = max(ans, dfs(r, c))
        return ans