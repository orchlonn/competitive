class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dp(i, cache):
            if i <= 1:
                return 
            
            if i in cache:
                return cache[i]
            
            cache[i] = min(dp(i - 1) + cost[i - 1], dp(i - 2) + cost[i - 2])
            return cache[i]
        
        return dp(len(cost), {})

# Time complexity: O(N)
# Space complexity: O(N)


# Solution 2: (Space optimized)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0, 0]

        for i in range(2, n + 1):
            tmp = min(dp[1] + cost[i - 1], dp[0] + cost[i - 2])
            dp[0] = dp[1]
            dp[1] = tmp

        return dp[1]

# Time complexity: O(N)
# Space complexity: O(1)