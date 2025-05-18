class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        temp_sum = sum(nums)

        if temp_sum % 2 != 0:
            return False
        
        target = temp_sum // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for i in range(target, num - 1, -1):
                if dp[i - num]:
                    dp[i] = True
        
        return dp[target]

# Time complexity: O(N^2)
# Space complexity: O(N)