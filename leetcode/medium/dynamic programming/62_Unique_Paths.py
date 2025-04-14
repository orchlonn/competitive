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
            print(cache[r][c])
            return cache[r][c]
        
        return dp(0, 0, m, n, [[0] * n for i in range(m)])
        
# Time complexity: O(M * N)
# Space complexity: O(M * N)