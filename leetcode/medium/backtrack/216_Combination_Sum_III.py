class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(comb, remain, nextIndex):
            if len(comb) == k and remain == 0:
                res.append(list(comb))
                return
            elif remain < 0:
                return
            
            for i in range(nextIndex, 9):
                comb.append(i + 1)
                backtrack(comb, remain - 1 - i, i + 1)
                comb.pop()

        res = []
        backtrack([], n, 0)
        return res

# Time complexity: O(2^n)
# Space complexity: O(2^n)