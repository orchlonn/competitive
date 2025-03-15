class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(i, curComb, curSum):
            if curSum == target:
                ans.append(curComb.copy())
                return
            
            if curSum > target:
                return
            
            if i > len(candidates):
                return
            
            for j in range(i, len(candidates)):
                curSum += candidates[j]
                curComb.append(candidates[j])
                backtrack(j, curComb, curSum)
                val = curComb.pop()
                curSum -= val

        ans = []
        backtrack(0, [], 0)
        return ans

# Time complexity: O(N^T), where N is the number of candidates and T is the target.
# Space complexity: O(T*X), where X is the number of valid combinations.