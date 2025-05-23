class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7
        cache = {} # (n, target) -> count

        def count(n, target):
            if n == 0:
                return 1 if target == 0 else 0
            
            if target < 0:
                return 0

            if (n, target) in cache:
                return cache[(n, target)]
            
            res = 0
            for val in range(1, k + 1):
                res = (res + count(n - 1, target - val)) % MOD
            
            cache[(n, target)] = res
            return res

        return count(n, target)

# Time complexity: O(N * K * Target)
# Space complexity: O(N * Target)


# Solution #2 
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (target + 1)
        dp[0] = 1

        for dice in range(n):
            next_dp = [0] * (target + 1)

            for val in range(1, k + 1):
                for total in range(val, target + 1):
                    next_dp[total] = (next_dp[total] + dp[total - val]) % MOD
            
            dp = next_dp
        
        return dp[-1]

# Time complexity: O(N * K * Target)
# Space complexity: O(Target)