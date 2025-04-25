class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        hold, free = [0] * n, [0] * n

        hold[0] = -prices[0]
        
        for i in range(1, n):
            hold = max(hold[i - 1], free[i - 1] - prices[i])
            free = max(free[i - 1], hold[i - 1] + prices[i] - fee)

        return free[-1]