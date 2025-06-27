class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = 0, 0
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break
        
        cur = 0
        while True:
            cur = nums[cur]
            slow = nums[slow]
            if cur == slow:
                return slow

# Time complexity: O(N)
# Space complexity: O(1)