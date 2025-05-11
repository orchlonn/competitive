class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])

        max_square = 0
        dp = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                if matrix[r][c] == "1":
                    dp[r][c] = 1 + min(dp[r + 1][c], dp[r][c + 1], dp[r + 1][c + 1])
                    max_square = max(max_square, dp[r][c])

        return max_square ** 2

# Time complexity: O(N^2)
# Space complexity: O(N^2)