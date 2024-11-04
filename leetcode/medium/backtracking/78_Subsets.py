class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(comb, i):
            if i > len(nums):
                return
            ans.append(list(comb))

            for j in range(i, len(nums)):
                comb.append(nums[j])
                backtrack(comb, j + 1)
                comb.pop()

        ans = []
        backtrack([], 0)
        return ans