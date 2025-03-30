class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True
        
        def backtrack(comb, index):
            if index >= n:
                res.append(comb.copy())
            
            for i in range(index, n):
                if isPalindrome(index, i):
                    comb.append(s[index:i + 1])
                    backtrack(comb, i + 1)
                    comb.pop()

        res = []
        n = len(s)
        backtrack([], 0)
        return res

# Time complexity: O(2^n * N)
# Space complexity: O(2^n * N)