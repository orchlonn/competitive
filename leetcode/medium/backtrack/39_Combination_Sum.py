class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(comb, i):
            if sum(comb) == target:
                ans.append(list(comb))
                return
            
            for j in range(i, len(candidates)):
                if sum(comb) < target:
                    comb.append(candidates[j])
                    backtrack(comb, j)
                    comb.pop()

        ans = []
        backtrack([], 0)
        return ans