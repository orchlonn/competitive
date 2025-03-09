class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        def backtrack(comb, i):
            if i > len(nums):
                return
            
            if list(comb) not in ans:
                ans.append(list(comb))

            for j in range(i, len(nums)):
                comb.append(nums[j])
                backtrack(comb, j + 1)
                comb.pop()

        ans = []
        backtrack([], 0)
        return ans