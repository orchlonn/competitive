class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = res = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        
        return res

# Time complexity: O(N)
# Space complexity: O(1) [Because count variable can take 26 alphabets]