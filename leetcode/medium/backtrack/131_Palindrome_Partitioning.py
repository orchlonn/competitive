class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True

        def backtrack(index, comb):
            if index >= n:
                res.append(comb.copy())
            
            for i in range(index, n):
                if isPalindrome(s, index, i):
                    comb.append(s[index:i + 1])
                    backtrack(i + 1, comb)
                    comb.pop()

        res = []
        n = len(s)
        backtrack(0, [])
        return res

# Time complexity: O(n * 2^n)
# Space complexity: O(n * 2^n)