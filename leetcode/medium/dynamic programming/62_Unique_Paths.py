class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dp(r, c, rows, cols, cache):
            if r == rows or c == cols:
                return 0
            
            if cache[r][c] > 0:
                return cache[r][c]
            
            if r == rows - 1 and c == cols - 1:
                return 1
            
            cache[r][c] = (dp(r + 1, c, rows, cols, cache) + dp(r, c + 1, rows, cols, cache))

            return cache[r][c]
        
        return dp(0, 0, m , n, [[0] * n for i in range(m)])
        
# Time complexity: O(M * N)
# Space complexity: O(M * N)


# Solution #2 (Bottom up)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0] * n
        
        for r in range(m - 1, -1, -1):
            curRow = [1] * n
            for c in range(n - 2, -1, -1):
                curRow[c] = curRow[c + 1] + dp[c]

            dp = curRow
        
        return dp[0]

# Time complexity: O(M * N)
# Space complexity: O(N)
