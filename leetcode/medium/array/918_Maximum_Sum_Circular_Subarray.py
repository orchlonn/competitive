class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globalMax, globalMin = nums[0], nums[0]
        curMax, curMin = 0, 0
        total = 0

        for n in nums:
            curMax = max(n, curMax + n)
            curMin = min(n, curMin + n)
            total += n

            globalMax = max(globalMax, curMax)
            globalMin = min(globalMin, curMin)
        
        return max(globalMax, total - globalMin) if globalMax > 0 else globalMax
    
# Time complexity: O(N)
# Space complexity: O(1)