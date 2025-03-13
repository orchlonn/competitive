class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(i, curComb):
            if len(curComb) >= k:
                comb.append(curComb.copy())
                return 
            
            if i > n:
                return
            
            for j in range(i, n + 1):
                curComb.append(j)
                dfs(j + 1, curComb)
                curComb.pop()

        comb = []
        dfs(1, [])
        return comb


# Time complexity: O(k * C(n, k)) 
# Space complexity: O(k) + O(C(n,k))

# where C = n!/k!(n-k)!