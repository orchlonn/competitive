class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def dfs(i, curSum):
            if curSum == amount:
                return 1
            if curSum > amount:
                return 0
            if i >= len(coins):
                return 0
            if (i, curSum) in cache:
                return cache[(i, curSum)]

            cache[(i, curSum)] = dfs(i, curSum + coins[i]) + dfs(i + 1, curSum)
            return cache[(i, curSum)]

        cache = {}
        return dfs(0, 0)

# Time complexity: O(n * amount)
# Space complexity: O(n * amount)