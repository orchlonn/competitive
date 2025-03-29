class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def dfs(subsequence, index):
            if len(subsequence) > 1:
                res.add(tuple(subsequence))
            
            if index == len(nums):
                return
            
            if not subsequence or nums[index] >= subsequence[-1]:
                dfs(subsequence + [nums[index]], index + 1)
            
            dfs(subsequence, index + 1)
        
        res = set()
        dfs([], 0)
        return list(res)

# Time complexity: O(2^n * n)
# Space complexity: O(2^n * n)