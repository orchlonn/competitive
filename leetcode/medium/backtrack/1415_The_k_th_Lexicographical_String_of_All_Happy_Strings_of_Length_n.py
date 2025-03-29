class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def generateHappyString(currStr):
            if len(currStr) == n:
                happyStr.append(currStr)
                return
            
            for currChar in ["a", "b", "c"]:
                if len(currStr) > 0 and currStr[-1] == currChar:
                    continue
                
                generateHappyString(currStr + currChar)

        happyStr = []
        generateHappyString("")

        if len(happyStr) < k:
            return ""
        
        return happyStr[k - 1]

# Time complexity: O(2^n)
# Space complexity: O(2^n)