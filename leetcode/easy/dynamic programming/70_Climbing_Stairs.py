class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(i):
            if i >= n:
                return i == n
            
            return dfs(i + 1) + dfs(i + 2)

        return dfs(0)

# Time complexity: O(N)
# Space complexity: O(N)


# Solutoin 2: Using DP-top to bottom
class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(i, cache):
            if i >= n:
                return i == n
            if i in cache:
                return cache[i]

            cache[i] = dfs(i + 1, cache) + dfs(i + 2, cache)
            return cache[i]
        return dfs(0, {})

# Time complexity: O(N)
# Space complexity: O(1)


# Solution 3: Using DP (Space optimized)
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        
        return one

# Time complexity: O(N)
# Space complexity: O(1)