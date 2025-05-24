# Solution 1:
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def dfs(i1, i2):
            if i1 == len(text1) or i2 == len(text2):
                return 0
            
            if (i1, i2) in cache:
                return cache[(i1, i2)]

            if text1[i1] == text2[i2]:
                cache[(i1, i2)] =  1 + dfs(i1 + 1, i2 + 1)
            else:
                cache[(i1, i2)] = max( dfs(i1 + 1, i2), 
                            dfs(i1, i2 + 1))

            return cache[(i1, i2)]

        cache = {}
        return dfs(0, 0)
        
# Time complexity: O(N * M)
# Space complexity: O(N * M)


# Soltution 2: (Bottom up - True dp solution)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n):
            for j in range(m):
                if text1[i] == text2[j]:
                    dp[i + 1][j + 1] = 1 + dp[i][j]
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
        
        return dp[-1][-1]

# Time complexity: O(N * M)
# Space complexity: O(N * M)

# Solution 3: (Optimized bottom up solution)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2): text1, text2 = text2, text1
        N, M = len(text1), len(text2)
        dp = [0] * (M + 1)

        for i in range(N):
            curRow = [0] * (M + 1)
            for j in range(M):
                if text1[i] == text2[j]:
                    curRow[j + 1] = 1 + dp[j]
                else:
                    curRow[j + 1] = max(dp[j + 1], curRow[j])
            dp = curRow

        return dp[-1]

# Time complexity: O(N * M)
# Space complexity: O(min(N,M))