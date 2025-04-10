class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for num in nums:
            tmp = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = tmp
        
        return rob2

# Time complexity: O(N)
# Space complexity: O(1)