class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        posDiagonal = set() # col - row
        negDiagnoal = set() # col + row
        res = 0

        def backtrack(r):
            if r == n:
                nonlocal res
                res += 1
                return

            for c in range(n):
                if c in col or (c - r) in posDiagonal or (c + r) in negDiagnoal:
                    continue
                    
                col.add(c)
                posDiagonal.add(c - r)
                negDiagonal.add(c + r)
                backtrack(r + 1)
                col.remove(c)
                posDiagonal.remove(c - r)
                negDiagonal.remove(c + r)
            
            backtrack(0)
            return res


