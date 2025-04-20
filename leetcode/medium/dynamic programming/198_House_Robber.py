class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(i):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            
            if i in cache: 
                return cache[i]
            
            cache[i] = max(dp(i - 1), dp(i - 2) + nums[i])
            return cache[i]

        cache = {}
        return dp(len(nums) - 1)

# Time complexity: O(N)
# Spcae complexity: O(N)

# Solution 2 (space optimized solution)
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for num in nums:
            tmp = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = tmp
        
        return rob2

# Time complexity: O(N)
# Space complexity: O(1)