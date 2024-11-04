class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(comb, i):
            if len(comb) == k:
                ans.append(list(comb))
                return 

            for num in range(i, n + 1):
                comb.append(num)
                backtrack(comb, num + 1)
                comb.pop()
            
        ans = []
        backtrack([], 1)
        return ans