class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(currStr, leftCount, rightCount):
            if len(currStr) == n * 2:
                res.append("".join(currStr))
                return
            
            if n > leftCount:
                currStr.append("(")
                backtrack(currStr, leftCount + 1, rightCount)
                currStr.pop()

            if leftCount > rightCount:
                currStr.append(")")
                backtrack(currStr, leftCount, rightCount + 1)
                currStr.pop()
        
        res = []
        backtrack([], 0, 0)
        return res

# Time Complexity: O(4^n/sqrt(n))
# Space complexity: O(n)