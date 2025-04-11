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