class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(numbers):
            rob1, rob2 = 0, 0

            for n in numbers:
                new_rob = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = new_rob
            
            return rob2 
        
        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))

# Time complexity: O(N)
# Space complexity: O(1)