class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1

        for i in range(len(nums)):
            next_dp = dp
            for curr_sum, count in dp:
                next_dp[curr_sum + nums[i]] += count
                next_dp[curr_sum - nums[i]] += count
            dp = next_dp
        
        return dp[target]

# Time complexity: O(N * T) where t = sum(nums)
# Space complexity: O(T)

# Solution #2: Top down
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ans = 0
        cache = {}
        N = len(nums)

        def dfs(i, curSum):
            if i == N:
                return 1 if curSum == target else 0

            if (i, curSum) in cache:
                return cache[(i, curSum)]

            cache[(i, curSum)] =  (
                dfs(i + 1, curSum + nums[i]) +
                dfs(i + 1, curSum - nums[i])
            )   

            return cache[(i, curSum)]

        return dfs(0, 0)

# Time complexity: O(N * T) where t = sum(nums)
# Space complexity: O(N * T)