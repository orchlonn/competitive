class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M, N = len(text1), len(text2)
        dp = [[0] * (N + 1) for i in range(M + 1)]
        dp[M - 1][N - 1] = 1

        for r in reversed(range(M)):
            for c in reversed(range(N)):
                if text1[r] == text2[c]:
                    dp[r][c] = dp[r + 1][c + 1] + 1
                elif c < N:
                    dp[r][c] = max(dp[r + 1][c], dp[r][c + 1])

        return dp[0][0]

# Time complexity: O(N * M)
# Space complexity: O(N * M)