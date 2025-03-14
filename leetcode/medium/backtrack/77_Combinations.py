class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(i, curComb):
            if len(curComb) >= k:
                ans.append(curComb.copy())
                return
            
            for j in range(i, n + 1):
                curComb.append(j)
                backtrack(j + 1, curComb)
                curComb.pop()

        ans = []
        backtrack(i, [])
        return ans

# Time complexity: O(k * C(n, k)) 
# Space complexity: O(k) + O(C(n,k))

# where C = n!/k!(n-k)!