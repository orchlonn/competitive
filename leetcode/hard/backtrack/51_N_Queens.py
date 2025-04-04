class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        comb = [["."] * n for i in range(n)]
        posDiag = set() # r + c
        negDiag = set() # r - c
        cols = set()

        def backtrack(r):
            if r == n:
                ans.append(["".join(row) for row in comb])
                return 

            for c in range(n):
                if c in cols or (r - c) in negDiag or (r + c) in posDiag or comb[r][c] == "Q":
                    continue
                        
                comb[r][c] = "Q"
                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                    
                backtrack(r + 1)

                comb[r][c] = "."
                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)

        backtrack(0)
        return ans

# Time complexity: O(N!)
# Space complexity: O(N^2) for comb + O(N) for backtracking. Thus, overall time complexity is O(N^2)