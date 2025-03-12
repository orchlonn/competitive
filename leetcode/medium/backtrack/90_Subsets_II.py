class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def backtrack(subsets, index, curSet):
            if index >= len(nums):
                subsets.append(curSet.copy())
                return

            # include nums[index]
            curSet.append(nums[index])            
            backtrack(subsets, index + 1, curSet)
            curSet.pop()

            # not include nums[index]
            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
            backtrack(subsets, index + 1, curSet)


        subsets, curSet = [], []
        backtrack(subsets, 0, curSet)
        return subsets

# Time complexity: O(n * 2^n)
# Space complexity: O(n) == O(h)