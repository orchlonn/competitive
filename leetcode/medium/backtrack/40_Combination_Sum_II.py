class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(comb, remain, index):
            if remain == 0:
                res.append(comb.copy())
                return
            elif remain < 0:
                return
            else:
                for i in range(index, len(candidates)):
                    if i > index and candidates[i] == candidates[i - 1]:
                        continue
                    if remain < candidates[i]:
                        break
                    comb.append(candidates[i])
                    backtrack(comb, remain - candidates[i], i + 1)
                    comb.pop()
        
        res = []
        candidates.sort()
        backtrack([], target, 0)
        return res

# Time complexity: O(2^n)
# Space complexity: O(2^n)