class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 0

        while len(nums) > r:
            count = 1

            while r + 1 < len(nums) and nums[r] == nums[r + 1]:
                r += 1
                count += 1
            
            for i in range(min(2, count)):
                nums[l] = nums[r]
                l += 1
            
            r += 1
        
        return l

# Time complexity: O(N)
# Space complexity: O(1)