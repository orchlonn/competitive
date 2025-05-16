class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        max_so_far = min_so_far = res = nums[0]

        for num in nums[1:]:
            if num < 0:
                max_so_far, min_so_far = min_so_far, max_so_far
            
            max_so_far = max(num, max_so_far * num)
            min_so_far = min(num, min_so_far * num)

            res = max(res, max_so_far)
        
        return res

# Time complexity: O(N)
# Space complexity: O(1)