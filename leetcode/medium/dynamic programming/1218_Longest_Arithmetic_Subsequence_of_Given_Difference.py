class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp_map = {}
        max_length = 0

        for num in arr:
            dp = dp_map.get(num - difference, 0) + 1
            dp_map[num] = dp
            max_length = max(max_length, dp)

        return max_length

# Time complexity: O(N)
# Space complexity: O(N)