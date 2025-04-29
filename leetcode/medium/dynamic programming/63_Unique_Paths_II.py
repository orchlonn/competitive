# Solution 1: Bottom up
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


# Solution 2: Top down
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        cache = {}

        def dfs(r, c):
            if r not in range(ROWS) or c not in range(COLS):
                return 0
            
            if obstacleGrid[r][c] == 1:
                return 0
            
            if (r, c) in cache:
                return cache[(r, c)]

            if r == ROWS - 1 and c == COLS - 1:
                return 1
            
            cache[(r ,c)] = (dfs(r + 1, c) + dfs(r, c + 1))
            return cache[(r, c)]
        
        return dfs(0, 0)

# Time complexity: O(COLS * ROWS)
# Space complexity: O(COLS)


