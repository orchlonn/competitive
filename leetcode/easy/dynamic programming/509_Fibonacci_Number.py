class Solution:
    def fib(self, n: int) -> int:
        def memoization(i, cache):
            if i <= 1:
                return i
            if i in cache:
                return cache[i]
            
            cache[i] = memoization(i - 2, cache) + memoization(i - 1, cache)
            return cache[i]
        
        return memoization(n, {})

# Time complexity: O(N)
# Space complexity: O(N)



# Solution 2
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        
        dp = [0, 1]
        i = 2
        while i <= n:
            tmp = dp[1]
            dp[1] = dp[1] + dp[0]
            dp[0] = tmp
            i += 1
        
        return dp[1]

# Time complexity: O(N)
# Space complexity: O(1)