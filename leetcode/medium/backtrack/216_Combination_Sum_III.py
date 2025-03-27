class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(remain, comb, nextStart):
            if remain == 0 and len(comb) == k:
                res.append(list(comb))
            elif remain < 0 or len(comb) == k:
                return

            for i in range(nextStart, 9):
                comb.append(i + 1)
                backtrack(remain - i - 1, comb, i + 1)
                comb.pop()

        res = []
        backtrack(n, [], 0)

        return res

# Time complexity: O(K * C(9, K))
# Space complexitiy: O(K)
