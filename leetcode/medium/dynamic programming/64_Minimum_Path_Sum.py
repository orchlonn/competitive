class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        @cache
        def dfs(r, c):
            if r + c == 0:
                return grid[r][c]

            ans = float('inf')
            if r > 0:
                ans = min(ans, dfs(r - 1, c))
            if c > 0:
                ans = min(ans, dfs(r, c - 1))

            return grid[r][c] + ans
            
        m = len(grid)
        n = len(grid[0])
        return dfs(m - 1, n - 1)
