class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
      res = []
      subset = []

      def dfs(index):
        if index >= len(nums):
          res.append(subset.copy())
          return
        
        # include nums[index]
        subset.append(nums[index])
        dfs(index + 1)

        # Not include nums[index]
        subset.pop()
        dfs(index + 1)
      
      dfs(0)
      return res

# Time complexity: O(2^n)
# Space complexity: O(n * 2^n)