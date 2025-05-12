class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def count_binary(s):
            zeros = s.count('0')
            ones = s.count('1')
            return zeros, ones

        def dfs(i, m, n):
            if i == len(strs):
                return 0
            
            if (i, m, n) in cache:
                return cache[(i, m, n)]
            
            zeros, ones = count_binary(strs[i])

            cache[(i, m, n)] = dfs(i + 1, m, n)

            if zeros <= m and ones <= n:
                cache[(i, m, n)] = max(
                    cache[(i, m, n)],
                    1 + dfs(i + 1, m - zeros, n - ones))
            return cache[(i, m, n)]
        
        cache = {}
        return dfs(0, m, n)

# Time complexity: O(k * m * n)
# Space complexity: O(k * m * n)