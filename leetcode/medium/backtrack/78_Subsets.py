class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(i, curSet):
            if i >= len(nums):
                res.append(curSet.copy())
                return
            
            # include nums[i]
            curSet.append(nums[i])
            backtrack(i + 1, curSet)
            curSet.pop()
            
            # not include nums[i]
            backtrack(i + 1, curSet)
        
        res = []
        backtrack(0, [])
        return res

# Time complexity: O(2^n)
# Space complexity: O(n) == O(h)