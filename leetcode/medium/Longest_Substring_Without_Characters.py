from collections import Counter

def lengthOfLongestSubstring(self, s: str) -> int:
    chars = Counter()
    left = right = 0
    
    res = 0
    while right < len(s):
        r = s[right]
        s[r] += 1
        
        while s[r] > 1:
            l = s[left]
            s[l] -= 1
            left += 1
        
        res = max(res, right - left + 1)
    
    return res