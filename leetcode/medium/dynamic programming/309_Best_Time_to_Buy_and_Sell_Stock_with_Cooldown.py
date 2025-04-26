class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            cooldown = dfs(i + 1, buying)
            if buying:
                hold = dfs(i + 1, not buying) - prices[i]
                dp[(i, buying)] = max(hold, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)

            return dp[(i, buying)]

        return dfs(0, True)

# Time complexity: O(N)