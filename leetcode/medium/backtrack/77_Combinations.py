class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(i, combs):
            if len(combs) >= k:
                res.append(combs.copy())
                return 
            
            for j in range(i, n + 1):
                combs.append(j)
                dfs(j + 1, combs)
                combs.pop()

        
        res = []
        dfs(1, [])
        return res


# Time complexity: O(k * C(n, k)) 
# Space complexity: O(k) + O(C(n,k))

# where C = n!/k!(n-k)!