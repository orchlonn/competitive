class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_list = [0] * len(nums) * 2
        for i in range(len(nums)):
            new_list[i] = nums[i]

        for i in range(len(nums)):
            new_list[len(nums) + i] = nums[i]


        return new_list 