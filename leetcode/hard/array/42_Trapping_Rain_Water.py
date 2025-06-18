class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        l, r = 0, len(height) - 1
        maxLeft, maxRight = height[l], height[r]
        ans = 0
        
        while r > l:
            if maxRight > maxLeft:
                l += 1
                maxLeft = max(maxLeft, height[l])
                ans += maxLeft - height[l]
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                ans += maxRight - height[r]
        
        return ans

# Time complexity: O(N)
# Space complexity: O(1)
