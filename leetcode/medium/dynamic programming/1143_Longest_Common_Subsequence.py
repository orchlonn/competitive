class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M, N = len(text1), len(text2)
        dp = [[0] * (N + 1) for i in range(M + 1)]

        for i in reversed(range(M)):
            for j in reversed(range(N)):
                if text1[i] == text2[j]:
                    print(i, j)
                    dp[i][j] += dp[i + 1][j + 1] + 1
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
    
        return dp[0][0]

# Time complexity: O(M * N)
# Space complexity: O(M * N)