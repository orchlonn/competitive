class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L, res = 0, 0
        q = deque()

        for R in range(len(s)):
            while s[R] in q:
                q.popleft()
                L += 1
            q.append(s[R])
            res = max(res, R - L + 1)
        
        return res

# Time complexity: O(N)
# Space complexity: O(N)