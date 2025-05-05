class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(numbers):
            first, second = 0, 0

            for num in numbers:
                temp = max(first + num, second)
                first = second
                second = temp
            
            return second

        return max(helper(nums[1:]), helper(nums[:-1]), nums[0])
# Time complexity: O(N)
# Space complexity: O(1)