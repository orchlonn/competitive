class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * COLS
        dp[-1] = 1

        for r in reversed(range(ROWS)):
            for c in reversed(range(COLS)):
                if obstacleGrid[r][c] == 1:
                    dp[c] = 0
                elif c + 1 < COLS:
                    dp[c] = dp[c] + dp[c + 1]

        return dp[0]

# Time complexity: O(COLS * ROWS)
# Space complexity: O(COLS)