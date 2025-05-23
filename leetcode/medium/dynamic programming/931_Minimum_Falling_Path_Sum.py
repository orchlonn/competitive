class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        cache = {}
        N = len(matrix)

        def dfs(r, c):
            if r == N:
                return 0
            
            if c == N or c < 0:
                return float('inf')
            
            if (r, c) in cache:
                return cache[(r, c)]
            
            res = matrix[r][c] + min(
                dfs(r + 1, c - 1),
                dfs(r + 1, c),
                dfs(r + 1, c + 1)
            )
            cache[(r, c)] = res
            return res
        
        ans = float('inf')
        for c in range(N):
            ans = min(ans, dfs(0, c))
        
        return ans

# Time complexity: O(N^2)
# Space complexity: O(N^2)

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        N = len(matrix)

        for r in range(1, N):
            for c in range(N):
                left = matrix[r - 1][c]
                mid = matrix[r - 1][c - 1] if c > 0 else float('inf')
                right = matrix[r - 1][c + 1] if c < N - 1 else float('inf')
                matrix[r][c] = matrix[r][c] + min(left, mid, right)
        
        return min(matrix[-1])

# Time complexity: O(N^2)
# Space complexity: O(1)