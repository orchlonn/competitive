# Solution 1
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                ans = max(ans, min(height[i], height[j]) * (j - i))
        
        return ans

# Time complexity: O(N^2)
# Space complexity: O(1)


# Solution 2: (Two pointers)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ans = 0

        while r > l:
            area = (r - l) * min(height[r], height[l])
            ans = max(ans, area)

            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
                
        return ans

# Time complexity: O(N)
# Space complexity: O(1)