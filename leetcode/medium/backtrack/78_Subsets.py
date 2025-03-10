class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subset = []

        def backtrack(index):
            if index >= len(nums):
                ans.append(subset.copy())
                return
            
            # include nums[index]
            subset.append(nums[index])
            backtrack(index + 1)

            # not include nums[index]
            subset.pop()
            backtrack(index + 1)
        
        backtrack(0)
        return ans

# Time complexity: O(2^n)
# Space complexity: O(n * 2^n)