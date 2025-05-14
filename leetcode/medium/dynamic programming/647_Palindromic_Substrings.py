class Solution:
    def countSubstrings(self, s: str) -> int:

        def expandAroundMiddle(left, right):
            count = 0 
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1
            return count 

        ans = 0
        for i in range(len(s)):
            ans += expandAroundMiddle(i, i) # Odd-length palindromes
            ans += expandAroundMiddle(i, i + 1) # Even-length palindromes
        
        return ans
        
# Time complexity: O(N^2)
# Space complexity: O(1)