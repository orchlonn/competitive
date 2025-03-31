class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        if len(s) > 12:
            return res
        
        def backtrack(dots, i, curIP):
            if dots == 4 and i == len(s):
                res.append(curIP[:-1])
                return
            
            if dots > 4:
                return
            
            for j in range(i, min(i + 3, len(s))):
                if int(s[i:j + 1]) < 256 and (i == j or s[i] != "0"):
                    backtrack(dots + 1, j + 1, curIP + s[i: j + 1] + ".")

        backtrack(0, 0, "")
        return res


# Time complexity: O(3^n)
    # However, the maximum n can be less or equal to 12. Thus, the time complexity is O(3^12) which is O(1).
# Space complexity: O(3^n). However, same thing applies here:  So, O(1)