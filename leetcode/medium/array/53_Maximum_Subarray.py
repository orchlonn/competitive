# Solution 1: Kadene's algorithm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        maxSum = nums[0]

        for num in nums:
            curSum = max(curSum, 0)
            curSum += num
            maxSum = max(curSum, maxSum)
        
        return maxSum
# Time complexity: O(N)
# Space complexity: O(1)