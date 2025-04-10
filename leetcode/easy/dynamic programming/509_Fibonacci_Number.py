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